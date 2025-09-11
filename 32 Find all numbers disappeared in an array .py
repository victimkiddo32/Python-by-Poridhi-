def findDisappearedNumbers(nums):
    dis_nums = []
    num_set = set(nums)
    for num in range(1, len(nums) + 1):
        if num not in num_set:
            dis_nums.append(num)
    return dis_nums

# main code
nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))