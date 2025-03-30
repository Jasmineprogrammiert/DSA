## Recursion
### Recursion
- when a function calls itself
- breaking problems into smaller easier subproblems
- Base case: where recursion stops

```javascript
function fib(n) { // loop: O(n)
  if (n < 1) return 0;
  if (n === 1) return 1;
  
  let prev = 1;
  let curr = 1;

  for (let i = 3; i <+ n; i++) {
    let next = curr + prev; // (n+1) = n + (n-1)
    prev = curr;
    curr = next;
  }

  return curr;
}
// 0, 1, 1, 2, 3, 5, 8, 13, 21 ---> num
// 0, 1, 2, 3, 4, 5, 6, 7, 8 ---> Index

// number at index 3 = number at index (2 + 1)
// 2 = 1 + 1
// n = n-1 + n-2

function fibRecursion(n) { // recursion: O(2^n)
  // base case
  if (n < 1) return 0;
  if (n === 1) return 1;

  // recursive calls
  return fibRecursion(n - 1) + fibRecursion(n - 2);
}

function fibMemorization(n, memo = {}) { // Memorizaion: 0(n)
  if (n in memo) return memo[n];

  // base case
  if (n < 1) return 0;
  if (n === 1) return 1;

  // recursive calls
  memo[n] = fibMemorization(n - 1, memo) + fibMemorization(n - 2, memo);

  return memo[n];
}
```

### Memorization
- the repeated calculation only get calculated once

### Additional
```javascript
function sayHello() {
  sayHello();
}

function countdown(num) {
  if (num <= 0) { // base case
    console.log("done!");
    return; // no more recursions
  }
  console.log(num);
  countdown(num - 1); // smaller number, easier
}

function infiniteRecursion() {
  infiniteRecursion();
}
```