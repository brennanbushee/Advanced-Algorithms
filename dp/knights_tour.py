from dp.n_queens_problem import conjoin


class Knights:
    def __init__(self, m, n, hard=0):
        self.m, self.n = m, n

        # solve() will set up succs[i] to be a list of square #i's
        # successors.
        succs = self.succs = []

        # Remove i0 from each of its successor's successor lists, i.e.
        # successors can't go back to i0 again.  Return 0 if we can
        # detect this makes a solution impossible, else return 1.

        def remove_from_successors(i0, len=len):
            # If we remove all exits from a free square, we're dead:
            # even if we move to it next, we can't leave it again.
            # If we create a square with one exit, we must visit it next;
            # else somebody else will have to visit it, and since there's
            # only one adjacent, there won't be a way to leave it again.
            # Finally, if we create more than one free square with a
            # single exit, we can only move to one of them next, leaving
            # the other one a dead end.
            ne0 = ne1 = 0
            for i in succs[i0]:
                s = succs[i]
                s.remove(i0)
                e = len(s)
                if e == 0:
                    ne0 += 1
                elif e == 1:
                    ne1 += 1
            return ne0 == 0 and ne1 < 2

        # Put i0 back in each of its successor's successor lists.

        def add_to_successors(i0):
            for i in succs[i0]:
                succs[i].append(i0)

        # Generate the first move.
        def first():
            if m < 1 or n < 1:
                return

            # Since we're looking for a cycle, it doesn't matter where we
            # start.  Starting in a corner makes the 2nd move easy.
            corner = self.coords2index(0, 0)
            remove_from_successors(corner)
            self.lastij = corner
            yield corner
            add_to_successors(corner)

        # Generate the second moves.
        def second():
            corner = self.coords2index(0, 0)
            assert self.lastij == corner  # i.e., we started in the corner
            if m < 3 or n < 3:
                return
            assert len(succs[corner]) == 2
            assert self.coords2index(1, 2) in succs[corner]
            assert self.coords2index(2, 1) in succs[corner]
            # Only two choices.  Whichever we pick, the other must be the
            # square picked on move m*n, as it's the only way to get back
            # to (0, 0).  Save its index in self.final so that moves before
            # the last know it must be kept free.
            for i, j in (1, 2), (2, 1):
                this  = self.coords2index(i, j)
                final = self.coords2index(3-i, 3-j)
                self.final = final

                remove_from_successors(this)
                succs[final].append(corner)
                self.lastij = this
                yield this
                succs[final].remove(corner)
                add_to_successors(this)

        # Generate moves 3 through m*n-1.
        def advance(len=len):
            # If some successor has only one exit, must take it.
            # Else favor successors with fewer exits.
            candidates = []
            for i in succs[self.lastij]:
                e = len(succs[i])
                assert e > 0, "else remove_from_successors() pruning flawed"
                if e == 1:
                    candidates = [(e, i)]
                    break
                candidates.append((e, i))
            else:
                candidates.sort()

            for e, i in candidates:
                if i != self.final:
                    if remove_from_successors(i):
                        self.lastij = i
                        yield i
                    add_to_successors(i)

        # Generate moves 3 through m*n-1.  Alternative version using a
        # stronger (but more expensive) heuristic to order successors.
        # Since the # of backtracking levels is m*n, a poor move early on
        # can take eons to undo.  Smallest square board for which this
        # matters a lot is 52x52.
        def advance_hard(vmid=(m-1)/2.0, hmid=(n-1)/2.0, len=len):
            # If some successor has only one exit, must take it.
            # Else favor successors with fewer exits.
            # Break ties via max distance from board centerpoint (favor
            # corners and edges whenever possible).
            candidates = []
            for i in succs[self.lastij]:
                e = len(succs[i])
                assert e > 0, "else remove_from_successors() pruning flawed"
                if e == 1:
                    candidates = [(e, 0, i)]
                    break
                i1, j1 = self.index2coords(i)
                d = (i1 - vmid)**2 + (j1 - hmid)**2
                candidates.append((e, -d, i))
            else:
                candidates.sort()

            for e, d, i in candidates:
                if i != self.final:
                    if remove_from_successors(i):
                        self.lastij = i
                        yield i
                    add_to_successors(i)

        # Generate the last move.
        def last():
            assert self.final in succs[self.lastij]
            yield self.final

        if m*n < 4:
            self.squaregenerators = [first]
        else:
            self.squaregenerators = [first, second] + \
                [hard and advance_hard or advance] * (m*n - 3) + \
                [last]

    def coords2index(self, i, j):
        assert 0 <= i < self.m
        assert 0 <= j < self.n
        return i * self.n + j

    def index2coords(self, index):
        assert 0 <= index < self.m * self.n
        return divmod(index, self.n)

    def _init_board(self):
        succs = self.succs
        del succs[:]
        m, n = self.m, self.n
        c2i = self.coords2index

        offsets = [( 1,  2), ( 2,  1), ( 2, -1), ( 1, -2),
                   (-1, -2), (-2, -1), (-2,  1), (-1,  2)]
        rangen = range(n)
        for i in range(m):
            for j in rangen:
                s = [c2i(i+io, j+jo) for io, jo in offsets
                                     if 0 <= i+io < m and
                                        0 <= j+jo < n]
                succs.append(s)

    # Generate solutions.
    def solve(self):
        self._init_board()
        from dp.n_queens_problem import conjoin
        for x in conjoin(self.squaregenerators):
            yield x

    def printsolution(self, x):
        m, n = self.m, self.n
        assert len(x) == m*n
        w = len(str(m*n))
        format = "%" + str(w) + "d"

        squares = [[None] * n for i in range(m)]
        k = 1
        for i in x:
            i1, j1 = self.index2coords(i)
            squares[i1][j1] = format % k
            k += 1

        sep = "+" + ("-" * w + "+") * n
        print(sep)
        for i in range(m):
            row = squares[i]
            print("|" + "|".join(row) + "|")
            print(sep)

if __name__ == '__main__':
    for c in conjoin([lambda: iter((0, 1))] * 3):
        print(c)

    k = Knights(8, 8)
    LIMIT = 2
    count = 0
    for x in k.solve():
        count += 1
        if count <= LIMIT:
            print("Solution", count)
            k.printsolution(x)
        else:
            break
    # [0, 0, 0]
    # [0, 0, 1]
    # [0, 1, 0]
    # [0, 1, 1]
    # [1, 0, 0]
    # [1, 0, 1]
    # [1, 1, 0]
    # [1, 1, 1]
