import random


if __name__ == '__main__':
    nums = [random.randint(0, 20) for _ in range(20)]
    print(nums)

    for i in range(1, len(nums)):
        # 将前n-i+1个数中的最大值逐步到末尾
        for j in range(len(nums) - i):
            # 前者比后者大则将较大值向后交换
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    print(nums)
