
nums = [34, 32, 11, 1, 0, 2, 5]


def find_sum(nums, target):
    for i in range(len(nums)):
        for n in range(len(nums)):
            if n != i:
                if nums[n] + nums[i] == target:
                    x = n
                    y = i
                    return x,y
                    break
                else:
                    pass
            else:
                pass


print(find_sum(nums, 12))

