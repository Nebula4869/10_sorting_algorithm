import random


if __name__ == '__main__':
    nums = [random.randint(0, 20) for _ in range(20)]
    print(nums)

    for i in range(len(nums)):
        # 找到后n-i个元素中的最小值并记录位置
        min_idx, min_num = i, nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] < min_num:
                min_idx, min_num = j, nums[j]
        # 将后n-i个元素中的最小值交换到位置i
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    print(nums)
