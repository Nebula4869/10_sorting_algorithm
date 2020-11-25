import random


if __name__ == '__main__':
    nums = [random.randint(0, 20) for _ in range(20)]
    print(nums)

    # 统计待排序列表中每一个元素的出现次数
    maximum, minimum = max(nums), min(nums)
    count = [0] * (maximum - minimum + 1)
    for num in nums:
        count[num - minimum] += 1

    # 统计每一个值左侧有多少个元素
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    res = [0] * len(nums)
    # 遍历待排序列表
    for i in range(len(nums)):
        # 当前元素值在计数列表中的位置
        idx = nums[i] - minimum
        # 根据元素值左侧元素数量将待排序元素放置在指定位置
        res[count[idx] - 1] = nums[i]
        # 计数列表对应位置-1
        count[idx] -= 1

    nums = res

    print(nums)
