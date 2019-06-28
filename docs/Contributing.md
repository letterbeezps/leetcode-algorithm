## Contributing

### Add Your Solution

Find a problem and complete your solution on [leetcode](https://leetcode.com).

Fork, then clone the repo:

`git clone https://github.com/your-username/leetcode-algorithm.git`

Enter the `leetcode` directory, create a new folder named after the first related topic of your problem, like: `Array, Hash Table`, `Graph` (Ignore this step if the folder already exists).

Create a folder inside the folder we create last step, The naming rules are like this(Ignore this step if the folder already exists).:

`question-number.littleCamelCaseTitle`

Add your solution inside the folder. The naming rules of your code file should be like this:

`question-numberlittleCamelCaseTitle.ext`

For example:

```
├── Graph // first related topic of your problem
│   ├── 279.numSquares // solution folder
│   │   └── 279numSquares.py // code
│   ├── SomePublicDataStructure.py
```

### Generate A New README

**DON'T modify the Table in the readme manually at any time.**

We can generate a new Table by using script.

Run:

`npm run g`

**Make sure that you have already installed `node.js` and the version is greater than 10.0.0**
