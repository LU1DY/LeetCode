nums = [2, 7, 11, 15]


def two_sum(array, target):
    for i, item in enumerate(array):
        complemento = target - item
        if complemento in array:
            for x, itemx in enumerate(array):
                if x == i or complemento != itemx:
                    continue
                else:
                    return [i, x]


print(two_sum(nums, 9))
