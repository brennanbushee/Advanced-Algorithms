class Queens:
    def __init__(self, n):
        self.n = n
        rangen = range(n)

        # Assign a unique int to each column and diagonal.
        # columns:  n of those, range(n).
        # NW-SE diagonals: 2n-1 of these, i-j unique and invariant along
        # each, smallest i-j is 0-(n-1) = 1-n, so add n-1 to shift to 0-
        # based.
        # NE-SW diagonals: 2n-1 of these, i+j unique and invariant along
        # each, smallest i+j is 0, largest is 2n-2.

        # For each square, compute a bit vector of the columns and
        # diagonals it covers, and for each row compute a function that
        # generates the possibilities for the columns in that row.
        self.rowgenerators = []
        for i in rangen:
            rowuses = [(1 << j) |  # column ordinal
                       (1 << (n + i - j + n - 1)) |  # NW-SE ordinal
                       (1 << (n + 2 * n - 1 + i + j))  # NE-SW ordinal
                       for j in rangen]

            def rowgen(rowuses=rowuses):
                for j in rangen:
                    uses = rowuses[j]
                    if uses & self.used == 0:
                        self.used |= uses
                        yield j
                        self.used &= ~uses

            self.rowgenerators.append(rowgen)

    # Generate solutions.
    def solve(self):
        self.used = 0
        for row2col in conjoin(self.rowgenerators):
            yield row2col

    def printsolution(self, row2col):
        n = self.n
        assert n == len(row2col)
        sep = "+" + "-+" * n
        print(sep)
        for i in range(n):
            squares = [" " for j in range(n)]
            squares[row2col[i]] = "Q"
            print("|" + "|".join(squares) + "|")
            print(sep)


def conjoin(gs):  # Flat conjoin
    n = len(gs)
    values = [None] * n
    iters = [None] * n
    _StopIteration = StopIteration  # make local because caught a *lot*
    i = 0
    while 1:
        # Descend.
        try:
            while i < n:
                it = iters[i] = gs[i]().__next__
                values[i] = it()
                i += 1
        except _StopIteration:
            pass
        else:
            assert i == n
            yield values

        # Backtrack until an older iterator can be resumed.
        i -= 1
        while i >= 0:
            try:
                values[i] = iters[i]()
                # Success!  Start fresh at next level.
                i += 1
                break
            except _StopIteration:
                # Continue backtracking.
                i -= 1
        else:
            assert i < 0
            break


if __name__ == '__main__':
    q = Queens(8)
    LIMIT = 2
    count = 0
    for row2col in q.solve():
        count += 1
        if count <= LIMIT:
            print("Solution", count)
            q.printsolution(row2col)
