# Contributing

We are open to, and grateful for, any contributions made by the community.

## Pull Requests

Pick a problem and complete your solution on [leetcode](https://leetcode.com).

Fork, then clone the repo:

```
git clone https://github.com/your-username/leetcode-algorithm.git
```

### Add Category Folder

Enter the `leetcode` directory.

If you'd like to add a new solution not in the readme list yet, you need to add category for it first, unless the category already exists.

The category folder named after the _first_ related topic of your problem, You can get it from the description of your problem on leetcode.

**examples:** `Graph`, `Array`, `BinaryTree`

### Add Algorithm Folder

Add a folder In the category folder ( Ignore this step if the folder already exists ).

**examples:** `1.twoSum`, `2.addTwoNumbers`,`279.numSquares`

### Add Code File

Add your code file inside the folder.

**examples:** `1twoSum.js`, `1twoSum.py`

The main argorithm file name **MUST start with the question number** on the leetcode. In order to facilitate the distinction between public code files and argorithm files.

### Directory Tree:

```shell
├── leetcode
│   ├── Graph // first related topic of your problem
│   ├── 279.numSquares // solution folder
│   │   └── 279numSquares.py // code
│   ├── SomePublicDataStructure.py
```

### Generate README

**DON'T** modify the table in the `README.md` manually at any time.

We can generate a new table by using script:

```shell
npm run readme
```

**Make sure that you have already installed `node.js` and the version is greater than 10.0.0**
