/**
 * @param {number} N
 * @return {number}
 */
var fib$1 = (N) => (N < 2 ? N : fib(N - 1) + fib(N - 2));

var fib$2 = function (N, memo = []) {
    if (N < 2) {
        return N;
    }

    if (memo[N] == null) {
        memo[N] = fib(N - 1, memo) + fib(N - 2, memo);
    }
    return memo[N];
};

// 黄金比例与斐波那契数列
var fib$3 = (N) =>
    Math.round(Math.pow((1 + Math.sqrt(5)) / 2, N) / Math.sqrt(5));

const fib = (N) => {
    if (N < 2) {
        return N;
    }
    let pre = 0;
    let current = 1;
    let next = 0;
    for (let i = 1; i < N; i++) {
        next = pre + current;
        pre = current;
        current = next;
    }
    return next;
};
