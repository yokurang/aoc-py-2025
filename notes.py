# curr = 50
# R150


def contains_repeated_nums(num):
    num_as_str = str(num)
    length = len(num_as_str)
    for i in range(1, length // 2 + 1):
        right = num_as_str[:i]
        if right * (length // i) == num_as_str:
            return True
    return False


print(contains_repeated_nums(10))
print(contains_repeated_nums(11))
print(contains_repeated_nums(111))
print(contains_repeated_nums(1010))
