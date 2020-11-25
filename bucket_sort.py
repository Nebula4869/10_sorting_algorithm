import random


if __name__ == '__main__':
    nums = [random.randint(0, 20) for _ in range(20)]
    print(nums)

    # 按固定范围划分桶
    maximum, minimum = max(nums), min(nums)
    buckets = [[] for i in range(maximum // 10 - minimum // 10 + 1)]

    # 根据范围将待排序列表映射至各桶中
    for i in nums:
        index = i // 10 - minimum // 10
        buckets[index].append(i)

    # 依次取回所有已排序的桶
    nums.clear()
    for bucket in buckets:
        nums.extend(sorted(bucket))

    print(nums)
