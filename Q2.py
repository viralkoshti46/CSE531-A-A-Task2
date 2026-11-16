def lcs_suffixes(sequence1, sequence2):
    # Return (LCS length, minimum total length of the two suffixes).
    raise NotImplementedError("Implement lcs_suffixes before running this template.")


def read_input():
    sequence1 = input().strip()
    sequence2 = input().strip()
    return sequence1, sequence2


if __name__ == "__main__":
    sequence1, sequence2 = read_input()
    lcs_length, total_length = lcs_suffixes(sequence1, sequence2)
    print(lcs_length)
    print(total_length)
