var convert = function(s, numRows) {
    if (numRows >= s.length || numRows == 1) {
        return s;
    }
    let rows = new Array(numRows);
    for (let i = 0; i < numRows; i++) {
        rows[i] = [];
    }
    let rowNum = 0;
    let step = 1;
    for (let i = 0; i < s.length; i++) {
        rows[rowNum].push(s[i]);
        if (rowNum == 0) {
            step = 1;
        } else if (rowNum == numRows - 1) {
            step = -1;
        }
        rowNum += step;
    }
    let strings = [];
    rows.map((item) => {
        strings.push(item.join(""));
    });
    const result = strings.join("");
    return result;
};