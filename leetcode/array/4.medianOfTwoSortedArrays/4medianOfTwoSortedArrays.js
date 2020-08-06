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

/**
 * 另一种方法，代码有点冗余 但是效率高
 *✔ Accepted
  ✔ 2085/2085 cases passed (116 ms)
  ✔ Your runtime beats 99.93 % of javascript submissions
  ✔ Your memory usage beats 89.04 % of javascript submissions (38.9 MB)
 */

var findMedianSortedArrays = function(nums1, nums2) {
    if (nums1.length > nums2.length) {
        [nums1, nums2] = [nums2, nums1];
    }
    const nums1Length = nums1.length,
        nums2Length = nums2.length;
    let iMin = 0,
        iMax = nums1Length;
    const halfLen = Math.floor((nums1Length + nums2Length + 1) / 2); // +1 这种情况单数时取 maxleft
    while (iMin <= iMax) {
        let i = Math.floor((iMin + iMax) / 2); //   二分查找
        let j = halfLen - i;
        if (i < iMax && nums2[j - 1] > nums1[i]) {
            iMin = i + 1;
        } else if (i > iMin && nums1[i - 1] > nums2[j]) {
            iMax = i - 1;
        } else {
            let maxLeft = 0;
            if (i === 0) {
                maxLeft = nums2[j - 1];
            } else if (j === 0) {
                maxLeft = nums1[i - 1];
            } else {
                maxLeft = Math.max(nums1[i - 1], nums2[j - 1]);
            }
            if ((nums1Length + nums2Length) % 2 === 1) {
                return maxLeft;
            }

            let minRight = 0;
            if (i === nums1Length) {
                minRight = nums2[j];
            } else if (j === nums2Length) {
                minRight = nums1[i];
            } else {
                minRight = Math.min(nums2[j], nums1[i]);
            }
            return (maxLeft + minRight) / 2;
        }
    }
    return 0;
};
