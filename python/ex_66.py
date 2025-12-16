digits_list = [9, 9, 9]


def plus_one(digits):
    digits[-1] += 1

    for i in range(len(digits) - 1, -1, -1):
        if i == 0 and digits[i] > 9:
            digits[i] = 1
            digits.append(0)
        elif digits[i] > 9:
            digits[i] = 0
            digits[i - 1] += 1

    return digits


print(plus_one(digits_list))