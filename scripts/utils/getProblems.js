const all = require('./all');

// 处理数据
const questionList = all.stat_status_pairs
    .map(item => ({
        title: item.stat.question__title,
        id: item.stat.question_id,
        path: item.stat.question__title_slug
    }))
    .sort((a, b) => a.id - b.id);

console.log(questionList);
module.exports = questionList;