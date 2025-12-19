def searchInsert(nums, target):
    left, rigth = 0, len(nums) - 1

    while left <= rigth:
        mid = (left + rigth) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            rigth = mid - 1

    return left


print(searchInsert([1,3,5,6], 7))
