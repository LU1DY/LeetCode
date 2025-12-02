nums = [0,0,1,1,1,2,2,3,3,4,5]

def removeDuplicates(nums):
    total = 1
    for i in range(len(nums) - 1):
        if not nums[i] == nums[i+1]:
            total += 1


    return total

print(removeDuplicates(nums))