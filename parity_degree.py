# A positive integer N is given. The goal is to find the highest power of 2 that divides N. In other words,
# we have to find the maximum K for which N modulo 2^K is 0.

# For example, given integer N = 24 the answer is 3, because 2^3 = 8 is the highest power of 2 that divides N.

# Write a function:

# def solution(N)

# that, given a positive integer N, returns the highest power of 2 that divides N.

# For example, given integer N = 24, the function should return 3, as explained above.

# Assume that:

# N is an integer within the range [1..1,000,000,000].
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

def get_parity_degree(N):
    two_degree_max = 0

    for degree in range(1, 10):
        power_two = 2 ** degree

        if N % power_two == 0:
            two_degree_max = degree
        elif power_two > N:
            break

    return two_degree_max


# print(get_parity_degree(24))  # 3 because 2^3 = 8
print(get_parity_degree(1000000000))  # 9
