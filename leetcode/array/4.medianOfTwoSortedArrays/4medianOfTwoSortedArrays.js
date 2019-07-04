// 找到两个有序数组中第N大的元素
const findNthEle = (nums1, nums2, n) => {
    const l1 = nums1.length,
        l2 = nums2.length;
    if (l1 > l2) {
        return findNthEle(nums2, nums1, n);
    }
    if (l1 === 0) {
        return nums2[n - 1];
    }
    if (n === 1) {
        return Math.min(nums1[0], nums2[0]);
    }
    let left = Math.min(n >> 1, l1),
        right = n - left;
    if (nums1[left - 1] < nums2[right - 1]) {
        return findNthEle(nums1.slice(left), nums2, right);
    } else {
        return findNthEle(nums1, nums2.slice(right), left);
    }
};

// 分奇偶讨论
var SOLUTION1_findMedianSortedArrays = (nums1, nums2) => {
    let len1 = nums1.length,
        len2 = nums2.length;
    if ((len1 + len2) % 2 === 1) {
        return findNthEle(nums1, nums2, ((len1 + len2) >> 1) + 1);
    }
    return (
        (findNthEle(nums1, nums2, (len1 + len2) >> 1) +
            findNthEle(nums1, nums2, ((len1 + len2) >> 1) + 1)) *
        0.5
    );
};

// 不分类讨论
var SOLUTION2_findMedianSortedArrays = (nums1, nums2) =>
    (findNthEle(nums1, nums2, (nums1.length + nums2.length + 1) >> 1) +
        findNthEle(nums1, nums2, (nums1.length + nums2.length + 2) >> 1)) /
    2;

// 简单粗暴
var CHEAT_findMedianSortedArrays = (nums1, nums2) => {
    const arr = nums1.concat(nums2).sort((a, b) => a - b);
    return (
        (arr[((arr.length + 1) >> 1) - 1] + arr[((arr.length + 2) >> 1) - 1]) /
        2
    );
};
