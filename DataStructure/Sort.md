# 排序

## 冒泡排序

>从序列一端开始往另一端冒泡，一次比较两个相邻的数的大小，两层循环，外层冒泡轮数，里层一次比较，时间复杂度$o(n^2)$

---

>**code**

``` python

def Bubble_Sort(arr: list[int]):
    for i in range(len(arr)):
        isSort = True  # 冒泡排序不关心原数据是否已经有序
        for j in range(len(arr)-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isSort = False
        if isSort:  # 原数据已经有序，直接结束
            break

```

## 选择排序

>先找到列表中最小的元素，将它和列表的第一个元素交换位置，第二步，在剩下的元素中继续寻找最小的元素，依次下去$o(n^2)$

---

>**code**

```python
def Select_sort(arr: list):
    for i in range(len(arr)):
        min = i  # 最小元素的坐标
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]  # 和待排序数组的第一个元素交换
```

## 插入排序

>把待排序列表分成，“已排序”和“未排序”两部分，初始状态就是已排序为空，为排序为整个列表，然后从未排序部分抽出一个数，有序的插入已排序部分（找到待插入的位置），直到全部排序，时间复杂度$O(n^2)$

---

>**code**

```python
def Insert_sort(arr: list):
    n = len(arr)
    for i in range(1, n):
        value = arr[i]
        j = i-1  # 待插入的位置
        while j >= 0:
            if arr[j] > value:
                a[j+1] = arr[j]  # 移动数组，也就是在寻找插入位置
            else:
                break
            j -= 1
        arr[j+1] = value
```

## 希尔排序

>又名 “缩小增量排序”，是插入排序的一种改进版本，因为插入排序对大规模的乱序数组的效率比较慢，因为每次只移动一个位置，希尔排序加快了插入的速度。让数据可以跳跃移动

---

>**code**

```python
def Shell_sort(arr: list):
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
```

## 归并排序

>核心思想：分治法，将一个数组分成两部分，递归分，知道分成单个元素，然后重新组装和合并。给你两个有序数组，将他们合并成一个新的有序数组，只有一个元素的数组肯定有序。

---

>**code**

```python
def merge_sort(arr: list):

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
```

## 快速排序

>核心思想：依然是分治法，每次从序列中选出一个基准值，一次和其它基准值做比较，大于基准值放右边，小的放左边

---

>**code**
递归

```python
def quicksort(array: list[int]):
    if len(array) < 2:
        return array  # 结束
    else:
        pivot = array[0]
        less = [i for i i array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quickosrt(less) + [pivot] + quicksort(greater)
```

---

>**code**
单边扫描

```python
def quick_sort(array):

    def partition(array, startIndex, endIndex):
        # 对这部分修改可以写双边扫描
        pivot = array[startIndex]  # 取基准值
        mark = startIndex  # 初始化下标
        for i in range(startIndex+1, endIndex+1):
            if array[i] < pivot:
                mark += 1
                array[i], array[mark] = array[mark], array[i]
        # 基准值与mark对应的元素调换位置
        array[startIndex] = array[mark]
        array[mark] = pivot

    def sort():
        if endIndex <= startIndex:
            return
        pivotIndex = partition(array, startIndex, endIndex)
        sort(array, startIndex, pviotIndex-1)
        sort(array, pviotIndex+1, endIndex)

    # 虽然依然使用了递归，但是都是在原数组上的操作
    sort(array, 0, len(array)-1)
```

>**code**
非递归+双边扫描

```python
def quick_sort(array):

    def partition(array, left, right):
        if not array or right <= 0 or left >= right:
            return
        pivot = array[left]
        i, j = left, right
        while i < j:
            while i < j and array[j] >= pivot:
                j -= 1
            array[i] = array[j]

            while i < j and array[i] <= pivot:
                i += 1
            a[j] = a[i]
        array[i] = pivot
        return i

    def Q_sort(array, left, right):
        if not array or right <= 0 or left >= right:
            return
        temp = []  # stack
        i, j = 0, 0
        temp.append(right)
        temp.append(left)
        while temp:
            i = temp.pop()
            j = temp.pop()
            if i < j:
                k = partition(array, i, j)
                if k > i:
                    temp.append(k-1)
                    temp.append(i)
                if j > k:
                    temp.append(j)
                    temp.append(k+1)

    Q_sort(array, 0, len(array)-1)
```

## 堆排序

> 把堆看作一颗完全二叉树，首先将待排序数组构造成完全二叉树。
接着就要将这颗没有规律的完全二叉树变成大根堆、小根堆，堆顶元素就是整棵树的最大值（最小值），对于子树也是如此。每次从堆顶取出元素后，重建整个堆（其实微调就可以了）

---

> **code**

```python
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

```

## 计数排序

```python
def Count_sort(self, arr: list):
        maxn = max(arr)

        countArr = [0] * (maxn+1)

        for index, num in enumerate(arr):
            countArr[num] += 1
            arr[index] = 0

        index = 0
        for i in range(len(countArr)):
            for _ in range(countArr[i]):
                arr[index] = i
                index += 1
```
