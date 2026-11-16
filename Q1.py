def modular_power(a, n, m):
    # Return the integer a^n modulo m in O(log n) time. 
    raise NotImplementedError("Implement modular_power before running this template.")


def read_input():
    a, n, m = map(int, input().split())
    return a, n, m


if __name__ == "__main__":
    a, n, m = read_input()
    result = modular_power(a, n, m)
    print(result)
