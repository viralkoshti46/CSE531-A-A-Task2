def minimum_spanning_forest(n, m, k, edges):
    # Return the minimum total weight of a spanning forest with at most k trees.
    # Required running time: O(m*log^2(n)) or better. 
    raise NotImplementedError("Implement minimum_spanning_forest before running this template.")


def read_input():
    n, m, k = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    return n, m, k, edges


if __name__ == "__main__":
    n, m, k, edges = read_input()
    total_weight = minimum_spanning_forest(n, m, k, edges)
    print(total_weight)
