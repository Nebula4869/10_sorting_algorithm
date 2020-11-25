import random


if __name__ == '__main__':
    nums = [random.randint(0, 20) for _ in range(20)]
    print(nums)

    # 初始化增量未n/2
    gap = len(nums) // 2
    while gap >= 1:
        # 以指定增量向后遍历形成当前子序列
        for i in range(gap, len(nums), gap):
            # 选取当前子序列第i个数
            j, num = i - gap, nums[i]
            # 将第i个数插入当前子序列前i个数中，前i个数已有序
            while j >= 0 and num < nums[j]:
                # 将当前子序列比待插入值大的数向后移动
                nums[j + gap] = nums[j]
                j -= gap
            # 插入当前子序列
            nums[j + gap] = num
        # 缩小增量
        gap //= 2

    print(nums)
