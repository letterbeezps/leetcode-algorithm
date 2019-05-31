const { readdir, stat } = require('fs').promises; // >= node 10.0.0
const { join, resolve } = require('path');
const rootPath = join(__dirname, '../');

/**
 * 递归遍历所有的文件 获取所有文件名称 以及相对根目录的路径
 * 扁平化后按照文件名前面的数字排序 （没有数字的不管） 按照扩展名分类
 * 写入readme
 */
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

// 获取指定扩展名相对当前项目根目录的相对路径
const getExtRelativePath = (extRegEx, list, rootPath) =>
    list
        .filter(path => path.match(extRegEx))
        .map(path => path.split(rootPath)[1]);

const classifyPath = async () => {
    const list = flattenDeep(
        await readDirRecursive(resolve(rootPath, 'leetcode'))
    );
    const allJs = getExtRelativePath(/\.js$/, list, rootPath);
    const allPy = getExtRelativePath(/\.py$/, list, rootPath);
    const allJava = getExtRelativePath(/\.java$/, list, rootPath);
    const pathObj = {
        javascript: allJs,
        python: allPy,
        java: allJava
    };

    return pathObj;
};

classifyPath();

const generateREADME = () => {};
