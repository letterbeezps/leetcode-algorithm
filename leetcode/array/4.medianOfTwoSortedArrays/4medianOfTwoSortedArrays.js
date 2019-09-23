/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = (nums1, nums2) => {
    const arr = nums1.concat(nums2).sort((a, b) => a - b);
    return arr.length % 2 === 0
        ? (arr[arr.length / 2] + arr[arr.length / 2 - 1]) / 2
        : arr[(arr.length - 1) / 2];
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
