/**
 * @param {string} secret
 * @param {string} guess
 * @return {string}
 */
var getHint = function (secret, guess) {
    let a = 0;
    let b = 0;
    const ds = [...Array(10)].fill(0);
    const dg = [...Array(10)].fill(0);
    for (let i = 0; i < secret.length; i++) {
        let [s, g] = [secret[i], guess[i]];
        if (s === g) {
            a += 1;
        }
        // 数字: 次数
        ds[s] += 1;
        dg[g] += 1;
    }

    // 值相同 / 位置相同  + 值相同 / 位置不同  = 值相同
    //       a           +       b  ?         =    ?
    // 相同的数字取出现次数较少的较小的
    for (let i = 0; i < ds.length; i++) {
        b += Math.min(ds[i], dg[i]);
    }

    b -= a;
    return a + 'A' + b + 'B';
};
