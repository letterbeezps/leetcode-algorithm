const { readdir, stat, open, writeFile } = require('fs').promises; // >= node 10.0.0
const { join, resolve } = require('path');
const allProblems = require('./utils/getProblems');
const difficultyMap = require('./utils/difficultyMap');

const rootPath = join(__dirname, '../');
const domain = `https://leetcode.com/problems/`;
const headerFields = ['Title', 'Solutions', 'Difficulty'];
/**
 * 递归遍历所有的文件 获取所有文件名称 以及相对根目录的路径
 * 扁平化后按照文件名前面的数字排序 （没有数字的不管） 按照扩展名分类
 * 写入readme
 */

// 递归获取所有文件路径
const readDirRecursive = async path => {
    return await readdir(path).then(async dirList => {
        // 获取path下所有的文件的状态
        const statList = await Promise.all(
            dirList.map(async item => await stat(resolve(path, item)))
        );
        return Promise.all(
            statList.map(async (stat, idx) =>
                // 如果是目录 递归 否则 返回路径
                stat.isDirectory()
                    ? await readDirRecursive(resolve(path, dirList[idx]))
                    : resolve(path, dirList[idx])
            )
        );
    });
};

// 扁平数组
const flattenDeep = arr =>
    arr.reduce(
        (acc, val) =>
            Array.isArray(val) ? acc.concat(flattenDeep(val)) : acc.concat(val),
        []
    );

// 获取题号
const getNumByPath = path => {
    const fileName = path.split('/')[path.split('/').length - 1];
    const nameWithoutNum = fileName.replace(/\d+/, '');
    const startNum = fileName.replace(nameWithoutNum, '');
    return startNum ? parseInt(startNum, 10) : '';
};
// 获取指定扩展名相对当前项目根目录的相对路径
const getExtRelativePath = (extRegEx, list, rootPath) =>
    list
        .filter(path => path.match(extRegEx))
        .map(path => path.split(rootPath)[1])
        .filter(path => getNumByPath(path))
        .sort((a, b) => getNumByPath(a) - getNumByPath(b));

const classifyPath = async () => {
    const list = flattenDeep(
        await readDirRecursive(resolve(rootPath, 'leetcode'))
    );
    const allJs = getExtRelativePath(/\.js$/, list, rootPath);
    const allPy = getExtRelativePath(/\.py$/, list, rootPath);
    const allJava = getExtRelativePath(/\.java$/, list, rootPath);
    const allC = getExtRelativePath(/\.c(pp)?$/, list, rootPath);
    const pathObj = {
        python: allPy,
        javascript: allJs,
        java: allJava,
        c: allC
    };

    return pathObj;
};

// 渲染表格边框
const renderLine = str =>
    str.replace(/[^\x00-\xff]/g, '--').replace(/[a-zA-Z]/g, '-');

// 将整个列表的表头修改成 title solutions difficulty solutions里面写每种语言的超链接
const renderSolutionHeader = _ => {
    const headerStr = headerFields.reduce(
        (acc, curr) => `${acc}  ${curr}  |`,
        `|  `
    );
    const headerBottom = headerFields.reduce(
        (acc, curr) => `${acc}  ${renderLine(curr)}  |`,
        `|  `
    );

    return `${headerStr}
${headerBottom}`;
};

const renderNewTable = pathObj => {
    const header = renderSolutionHeader();
    const tableMatrix = {};
    // 遍历每一个数组 扔到一个对象的属性数组对应题号的位置
    // k: 语言名称 v: 路径数组
    Object.entries(pathObj).map(([k, v]) => {
        tableMatrix[k] = [];
        v.forEach(path => {
            tableMatrix[k][getNumByPath(path)] = `[${
                k
                // path.split('/')[path.split('/').length - 1]
            }](${path})`;
        });
    });
    const matrixArr = Object.entries(tableMatrix);
    // 找到属性数组中最长的 遍历这个数组  如果对应的所有的属性数组中的对应index选项都不为空 渲染行
    const sortList = Object.entries(tableMatrix)
        .map(([k, v]) => ({
            lang: k,
            length: v.filter(item => item).length
        }))
        .sort((a, b) => b.length - a.length);
    let tableStr = ``;
    tableMatrix[sortList[0].lang].forEach((item, idx, arr) => {
        // 如果每门语言该题都为空
        if (matrixArr.every(([k, v]) => !v[idx])) {
        } else {
            // 否则 拼接表格的行
            let tableRow = matrixArr.reduce(
                (acc, [k, v], index, srcArr) =>
                    v[idx]
                        ? `  ${acc}${index === 0 ? '' : ','} ${v[idx]}`
                        : `${acc}`,
                `|  [${idx}. ${allProblems[idx - 1].title}](${domain}${
                    allProblems[idx - 1].path
                })  |`
            );

            tableRow =
                tableRow +
                `|  ${difficultyMap[allProblems[idx - 1].difficulty]}  |`;

            tableStr = `${tableStr}
${tableRow}`;
        }
    });

    return `${header}${tableStr}`;
};

// 生成新的readme
const generateREADME = async () => {
    const pathObj = await classifyPath();
    const titleText = `# LeetCode
`;
    renderNewTable(pathObj);

    const dataToWrite = `${titleText}
${renderNewTable(pathObj)}`;
    await open('README.md', 'w')
        .then(fd => {
            writeFile(fd, dataToWrite, {
                flag: 'w'
            }).then(e => {
                if (e) throw e;
            });
        })
        .catch(e => {
            throw e;
        });
};

generateREADME();
