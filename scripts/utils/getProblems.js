const all = require('./all');

// 处理数据
const questionObj = {};

all.stat_status_pairs
    .map(item => ({
        title: item.stat.question__title,
        id: item.stat.question_id,
        path: item.stat.question__title_slug,
        difficulty: item.difficulty.level,
        frontId: item.stat.frontend_question_id
    }))
    .forEach(item => {
        questionObj[item.frontId] = item;
        questionObj[item.id] = item;
        
    });

module.exports = questionObj;
