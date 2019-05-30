const fs = require('fs');
const { join, resolve } = require('path');

const rootPath = join(__dirname, '../');
const getAllFiles = path => {
    return new Promise((resolve, reject) => {
        fs.readdir(path, (err, list) => {
            if (err) {
                reject(err);
            }
            resolve(list);
        });
    });
};

const getStats = dir => {
    return new Promise((resolve, reject) => {
        fs.stat(dir, (err, stats) => {
            if (err) {
                reject(err);
            }
            resolve(stats);
        });
    });
};

const fileRead = path => {
    return new Promise((resolve, reject) => {
        fs.readFile(path, (err, data) => {
            if (err) {
                reject(err);
            }
            resolve(data);
        });
    });
};

const mkDir = dir => {
    return new Promise((resolve, reject) => {
        fs.mkdir(dir, { recursive: false }, err => {
            if (err) {
                reject(err);
            }
            resolve();
        });
    });
};

getAllFiles(resolve(rootPath, 'leetcode'))
    .then(async data => {
        const statsList = await Promise.all(
            data.map(async item => {
                const catePath = resolve(rootPath, 'leetcode', item);
                return await getStats(catePath);
            })
        );
        return data.filter((item, idx, array) => {
            return statsList[idx].isDirectory();
        });
    })
    .then(async list => {
        // 题目路径
        const pathList = list.map(item => {
            const catePath = resolve(rootPath, 'leetcode', item);
            return catePath;
        });
        // 所有*py代码的文件名
        const nameList = await Promise.all(
            pathList.map(async path => {
                return await getAllFiles(resolve(__dirname, path));
            })
        );
        // console.log(nameList, '🧶');
        nameList.map((dir, idx) => {
            return dir.map(async fileName => {
                console.log(fileName.split('.')[0]);
                await mkDir(
                    `leetcode/${pathList[idx]}/${fileName.split('.')[0]}`
                );
                // return await mkDir(fileName.split('.')[0])
            });
        });
    })
    .catch(err => {
        console.log(err);
    });
