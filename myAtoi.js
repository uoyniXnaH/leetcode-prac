var myAtoi = function(s) {
    const r = /^[+-]?\d+/;
    const m = s.trim().match(r);
    if (!m) {
        return 0
    } else {
        let result = parseInt(m[0], 10);
        if (result < -2147483648) {
            result = -2147483648
        }
        if (result > 2147483647) {
            result = 2147483647
        }
        return result
    }
};