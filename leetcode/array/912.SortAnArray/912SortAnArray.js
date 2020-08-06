/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray$1 = function (nums) {
    function qs(nums, left, right) {
        if (left >= right) {
            return;
        }
        let mid = (left + right) >> 1;
        let pivot = nums[mid];
        let i = left - 1;
        let j = right + 1;
        while (i < j) {
            i++;
            while (nums[i] < pivot) {
                i++;
            }
            j--;
            while (nums[j] > pivot) {
                j--;
            }
            if (i < j) {
                [nums[i], nums[j]] = [nums[j], nums[i]];
            }
        }
        qs(nums, left, j);
        qs(nums, j + 1, right);
    }
    qs(nums, 0, nums.length - 1);
    return nums;
};

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray$2 = function (nums) {
    function qs(nums, left, right) {
        const stack = [[left, right]];
        while (stack.length > 0) {
            const [l, r] = stack.pop();
            if (l >= r) {
                continue;
            }
            let mid = (l + r) >> 1;
            let pivot = nums[mid];
            let i = l - 1;
            let j = r + 1;
            while (i < j) {
                i++;
                while (nums[i] < pivot) {
                    i++;
                }
                j--;
                while (nums[j] > pivot) {
                    j--;
                }
                if (i < j) {
                    [nums[i], nums[j]] = [nums[j], nums[i]];
                }
            }
            stack.push([j + 1, r]);
            stack.push([l, j]);
        }
    }
    qs(nums, 0, nums.length - 1);
    return nums;
};

var sortArray$3 = function (nums) {
    function bubble(nums) {
        const len = nums.length;
        for (let i = 0; i < len; i++) {
            for (let j = i + 1; j < len; j++) {
                if (nums[i] > nums[j]) {
                    [nums[i], nums[j]] = [nums[j], nums[i]];
                }
            }
        }
    }
    bubble(nums);
    return nums;
};
var sortArray$4 = function (nums) {
    function insert(nums) {
        const len = nums.length;
        let cur, j;
        for (let i = 0; i < len; i++) {
            cur = nums[i];
            j = i;
            while (nums[j - 1] > cur && j > 0) {
                nums[j] = nums[j - 1];
                j--;
            }
            nums[j] = cur;
        }
    }
    insert(nums);
    return nums;
};
