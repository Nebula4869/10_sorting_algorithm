import random


if __name__ == '__main__':
    nums = [random.randint(0, 20) for _ in range(20)]
    print(nums)

    def helper(s):
        # 只有一个数字或空时结束递归
        if len(s) <= 1:
            return s

        # 分别排序左右两半部分
        mid = len(s) // 2
        left = helper(s[:mid])
        right = helper(s[mid:])

        # 将左右两部分有序合并
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(right[j:])
        merged.extend(left[i:])
        return merged
    # 开始递归
    nums = helper(nums)

    print(nums)
