## Algo Efficiency & Big O Notation
### Time Complexity
- Big O doesn't care about the exact number of operations, it cares about the relationship between time complexity and n
- i.e how the number of operations grows as the input size increases

```javascript
// Constant time O(1)
function sumToNFormula(n) {
  return (n * (n + 1)) / 2;
}

// Linear time O(n)
function sumToNLoop(n) {
  let total = 0;

  for (let i = 1; i <= n; i++) total += i;
  return total;
}

// Quadratic time O(n^2)
function printAllPairs(arr) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length; j++) {
      console.log(arr[i], arr[j]);
    }
  }
}

// Logarithmic time O(log n)
// Since the size of the array is halved in each iteration, and the loop runs approximately log2(n) times, the overall time complexity of the function is O(log n)
function middleValues(arr) {
  let midVals = [];
  let end = arr.length - 1;

  while (end > 0) {
    let mid = Math.floor(end / 2);
    midVals.push(arr[mid]);
    end = mid;
  }
  return midVals;
}
```

### Space Complexity
- Memory usage
- The total amount of memory space required by the algorithm to execute
- Extra space used by the algorithm + input space

```javascript
// Constant space O(1)
function addNumbers(a, b) {
  return a + b;
}

// Linear space O(n)
function createNumberList(n) {
  let numberList = [];

  for (let i = 0; i < n; i++) {
    numberList.push(i);
  }
  return numberList;
}

// Quadratic space O(n^2)
function createPairs(n) {
  let pairs = [];

  for (let i = 0; i < n; i++) {
    let rows = [];

    for (let j = 0; j < n; j++) {
      row.push([i, j]);
    }
    pairs.push(row);
  }
  return pairs;
}
```

### Additional
```javascript
// Given n, the total number of steps in a staircase, and the ability to climb either 1 or 2 steps at a time. How many ways are there to reach the top of the staircase?
function countStaircaseWays(n) { // Time complexity: O(n) linear time
  if (n === 0) return 0
  if (n === 1) return 1;
  if (n === 2) return 2;

  // variables starting from step 3
  let waysToPrevStep = 2; // n - 1 (ways to reach step 2)
  let waysToPrevTwoSteps = 1; // n - 2 (ways to reach step 1)
  let count = 0; 

  for (i = 3; i <= n; i++) {
    // ways(n) = ways(n - 1) + ways(n - 2)
    count = waysToPrevStep + waysToPrevTwoSteps;
    waysToPrevTwoSteps = waysToPrevStep;
    waysToPrevStep = count;
  }

  return count;
}

countStaircaseWays(0); // 0: []
countStaircaseWays(1); // 1: [1]
countStaircaseWays(2); // 2: [1, 1], [2]
countStaircaseWays(3); // 3: [1, 1, 1], [1, 2], [2, 1]
countStaircaseWays(4); // 5: [1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]
countStaircaseWays(5); // 8: [1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 2, 1], [1, 2, 1, 1], [2, 1, 1, 1], [1, 2, 2], [2, 1, 2], [2, 2, 1]
```