def shortest_path(n, m, edges): 
    # Return the integer shortest-path length from vertex 1 to vertex 2.
    # Return the string "INFINITY" if no such path exists.
    # Required running time: O(n^2+m log n) or better for the stated input bounds. 
    raise NotImplementedError("Implement shortest_path before running this template.")


def read_input():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    return n, m, edges


if __name__ == "__main__":
    n, m, edges = read_input()
    result = shortest_path(n, m, edges)
    print(result)
