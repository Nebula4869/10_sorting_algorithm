import random
import math


if __name__ == '__main__':
    nums = [random.randint(0, 20) for _ in range(20)]
    print(nums)

    radix = 10
    k = math.ceil(math.log(max(nums) + 1, radix))

    buckets = [[] for i in range(radix)]

    for i in range(k):
        # 根据元素的第i位映射至各桶中
        for num in nums:
            buckets[(num // (radix ** i)) % radix].append(num)

        # 依次取回根据第i位分组的各桶元素
        nums.clear()
        for bucket in buckets:
            nums.extend(bucket)
            bucket.clear()

    print(nums)
