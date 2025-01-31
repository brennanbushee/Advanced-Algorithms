def find_first_different_letter(word1, word2):
    size = min(len(word1), len(word2))
    for i in range(size):
        if (word1[i] != word2[i]):
            return word1[i], word2[i]
    return None


def visit(v, adj, stack, visited, order):
    if (visited[v]):
        return True
    if (stack[v]):
        return False
    stack[v] = True
    for u in adj[v]:
        if (stack[u]):
            print(f"Found a cycle: u = {u}")
            return False
        print(f"Now visiting {u}")
        visit(u, adj, stack, visited, order)
    stack[v] = False
    visited[v] = True
    order.insert(0, v)
    return True


def find_order(words):
    """
    Args:
     words(list_str)
    Returns:
     str
    """
    # Write your code here.
    adj = {}
    for w in words:
        for c in w:
            if (c not in adj):
                adj[c] = []
    for i in range(1, len(words)):
        char = find_first_different_letter(words[i - 1], words[i])
        if char:
            adj[char[0]].append(char[1])
    visited = {x: False for x in adj}
    stack = {x: False for x in adj}
    order = []
    for i, c in enumerate(adj):
        if not visited[c]:
            visit(c, adj, stack, visited, order)
    return ''.join(order)

print(find_order(["baa", "abcd", "abca", "cab", "cad"]))#-> "bdac"
print(find_order(["caa", "aaa", "aab"])) #-> "cab"