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