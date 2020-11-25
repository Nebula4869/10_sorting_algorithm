import random


if __name__ == '__main__':
    nums = [random.randint(0, 20) for _ in range(20)]
    print(nums)

    def adjust_heap(parent, end):
        temp = nums[parent]  # 记录初始父节点
        child = 2 * parent + 1  # 选取左孩子
        while child < end:
            # 确保选取最大的左孩子
            if child + 1 < end and nums[child] < nums[child + 1]:
                child += 1
            # 如果左孩子大于父节点，则交换
            if temp <= nums[child]:
                nums[parent] = nums[child]
                parent = child
                child = 2 * parent + 1
            else:
                break
        # 存储初始父节点
        nums[parent] = temp

    # 构建大顶堆
    for i in range(len(nums) // 2 - 1, -1, -1):
        adjust_heap(i, len(nums))
        print(nums)

    for j in range(len(nums) - 1, 0, -1):
        # 将堆顶元素即前j + 1个元素中的最大值交换至j处
        nums[0], nums[j] = nums[j], nums[0]
        # 对前j个元素构建大顶堆
        adjust_heap(0, j)

    print(nums)
