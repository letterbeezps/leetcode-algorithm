import json
class Solution:

    def Bubble_Sort(self, arr: list):
        print('test', arr)
        for i in range(len(arr)):
            isSort = True  # 冒泡排序不关心原数据是否已经有序
            for j in range(len(arr)-i-1):
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    isSort = False
            if isSort:  # 原数据已经有序，直接结束
                break

    def Select_sort(self, arr: list):
        for i in range(len(arr)):
            min = i  # 最小元素的坐标
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min]:
                    min = j
            arr[min], arr[i] = arr[i], arr[min]  # 和待排序数组的第一个元素交换

    def Insert_sort(self, arr: list):
        n = len(arr)
        for i in range(1, n):
            value = arr[i]
            j = i-1  # 待插入的位置
            while j >= 0:
                if arr[j] > value:
                    arr[j+1] = arr[j]  # 移动数组，也就是在寻找插入位置
                else:
                    break
                j -= 1
            arr[j+1] = value

    def Shell_sort(self, arr: list):
        length = len(arr)
        gap = 1  # 区间，可以自己决定
        while gap < length:
            gap = gap * 3 + 1
        while gap > 0:  # 插入排序是一种特殊的希尔排序
            for i in range(gap, length):
                tmp = arr[i]
                j = i - gap
                while j >= 0 and arr[j] > tmp:
                    arr[j+gap] = arr[j]
                    j -= gap
                arr[j + gap] = tmp
            gap = gap // 3

    def merge_sort(self, arr: list):
    
        def merge(arr, tempArr, start, mid, end):
            tempArr[start:end+1] = arr[start:end+1]
            left, right = start, mid+1
            for k in range(start, end+1):
                if left > mid:
                    arr[k] = tempArr[right]
                    right += 1
                elif right > end:
                    arr[k] = tempArr[left]
                    left += 1
                elif tempArr[right] < tempArr[left]:
                    arr[k] = tempArr[right]
                    right += 1
                else:
                    arr[k] = tempArr[left]
                    left += 1

        def sort(arr, tempArr, start, end):
            if start >= end:
                return
            mid = start + (end - start) // 2
            sort(arr, tempArr, start, mid)
            sort(arr, tempArr, mid+1, end)
            merge(arr, tempArr, start, mid, end)
        # start sort()
        tempArr = [0] * len(arr)
        sort(arr, tempArr, 0, len(arr)-1)


    def Heap_sort(self, arr: list):

        def sink(arr: list, index: int, length: int):
            # 原始数据的顺序，作为初始化树的层次遍历顺序，然后再把这棵树变成大根堆。
            leftChild = 2*index + 1
            rightChild = 2*index + 2
            present = index

            if leftChild < length and arr[leftChild] > arr[present]:
                present = leftChild

            if rightChild < length and arr[rightChild] > arr[present]:
                present = rightChild

            if present != index:  # 下标不等，意味着需要调换元素值
                arr[index], arr[present] = arr[present], arr[index]
                sink(arr, present, length)

        def buildHeap(arr: list, length: int):
            # 此处构建完全二叉树，下标是以0 开始的
            for i in range(length//2-1, -1, -1):  # 从最后一个叶子结点的父节点开始调整整棵树
                sink(arr, i, length)


        length = len(arr)
        buildHeap(arr, length)
        print('init_heap', arr)
        for i in range(length-1, 0, -1):
            arr[0],arr[i] = arr[i], arr[0]
            length -= 1
            sink(arr, 0, length)


def stringToIntegerList(input):
    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line)

            # Solution().Bubble_Sort(nums)
            # print('Bubble_sort_res', nums)

            # Solution().Select_sort(nums)
            # print('Select_sort_res', nums)

            # Solution().Insert_sort(nums)
            # print('Insert_sort_res',nums)

            # Solution().Shell_sort(nums)
            # print('Shell_sort_res', nums)

            # Solution().merge_sort(nums)
            # print('merge_sort_res', nums)

            # Solution().Heap_sort(nums)
            # print('heap_sort_res', nums)
            
            
        except StopIteration:
            break

if __name__ == '__main__':
    main()