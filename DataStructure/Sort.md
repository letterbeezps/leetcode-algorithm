# 排序

## 冒泡排序

>从序列一端开始往另一端冒泡，一次比较两个相邻的数的大小，两层循环，外层冒泡轮数，里层一次比较，时间复杂度$o(n^2)$

---

>**code**

``` python

def Bubble_Sort(arr: list[int]):
    for i in range(len(arr)):
        isSort = True  # 冒泡排序不关心原数据是否已经有序
        for j in range(len(arr)-i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isSort = fasle
        if isSort:  # 原数据已经有序，直接结束
            break

```

## 选择排序

>先找到列表中最小的元素，将它和列表的第一个元素交换位置，第二步，在剩下的元素中继续寻找最小的元素，依次下去$o(n^2)$

---

>**code**

```python
def Select_sort(arr: List[int]):
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
def Insert_sort(arr: List[int]):
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
def Shell_sort(arr: List[int]):
    int length = len(arr)
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

>核心思想：分治法，将一个数组分成两部分，递归分，知道分成单个元素，然后重新组装和合并

---

>**code**

```python
def merge_sort(arr: List[int]):

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
