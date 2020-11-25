import random


if __name__ == '__main__':
    nums = [random.randint(0, 20) for _ in range(20)]
    print(nums)

    def helper(left, right):
        # 待处理的区域为空则结束迭代
        if left >= right:
            return

        # 选取一个元素作为中间值并记录
        mid_num = nums[left]
        # 初始化左右指针，左指针初始位置为中间值位置
        i = left
        j = right
        while i < j:

            # 右指针向左扫描，找出一个小于中间值的元素
            while i < j and nums[j] >= mid_num:
                j -= 1
            # 将小于中间值的元素交换到左指针位置
            nums[i] = nums[j]

            # 左指针向右扫描，找出一个大于等于中间值的元素
            while i < j and nums[i] < mid_num:
                i += 1
            # 将大于等于中间值的元素交换到右指针位置
            nums[j] = nums[i]

        # 指针交汇点左边均小于中间值，右边均大于等于中间值，将记录的中间值放置在指针交汇点
        nums[i] = mid_num

        # 以中间值为界，两边分别处理
        helper(left, i - 1)
        helper(i + 1, right)

    helper(0, len(nums) - 1)

    print(nums)
