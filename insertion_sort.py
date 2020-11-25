import random


if __name__ == '__main__':
    nums = [random.randint(0, 20) for _ in range(20)]
    print(nums)

    for i in range(1, len(nums)):
        # 选取第i个数
        j, num = i - 1, nums[i]
        # 将第i个数插入前i个数中，前i个数已有序
        while j >= 0 and num < nums[j]:
            # 将比待插入值大的数向后移动
            nums[j + 1] = nums[j]
            j -= 1
        # 插入
        nums[j + 1] = num

    print(nums)
