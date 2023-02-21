# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

# For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has
# binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20
# has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation
# 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

# Write a function:

# def solution(N)

# that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if
# N doesn't contain a binary gap.

# For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and
# so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary
# representation '100000' and thus no binary gaps.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..2,147,483,647].


def get_parking_bill(start, end):
    extra_hours = 0

    parking_time_minutes = int(end[-2:]) - int(start[-2:])
    parking_time_hours = int(end[:2]) - int(start[:2])

    if parking_time_hours >= 1:
        extra_hours = parking_time_hours - 1
        if parking_time_minutes > 0:
            extra_hours += 1

    parking_time = 2 + 3 + (extra_hours * 4)
    return (parking_time)


# print(get_parking_bill("10:00", "13:21"))  # 2 + 3 + (3 * 4) = 17
# print(get_parking_bill("10:00", "10:21"))  # 2 + 3 = 5
# print(get_parking_bill("10:00", "13:00"))  # 2 + 3 + (2 * 4) = 13
print(get_parking_bill("10:00", "11:20"))  # 2 + 3 + 4 = 9
