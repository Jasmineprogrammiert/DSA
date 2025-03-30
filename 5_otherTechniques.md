## Other Techniques
### Divide & Conquer
- breaking a problem into smaller subproblems
- works well with recursion

```javascript
// find the largest number in a given array of integers

function findLargestNumber(arr) {
  // base case
  if (arr.length === 1) return arr[0];

  const mid = Math.floor(arr.length / 2);
  const left = arr.slice(0, mid);
  const right = arr.slice(mid);

  // recursive step
  const leftMax = findLargestNumber(left);
  const rightMax = findLargestNumber(right);

  return Math.max(left, right);

}
```

### Dynamic Programming
- breaking a problem into smaller subproblems
- remember results of previously calculated subproblems
- use memotization to do this

```javascript
// give a grid of dimension m * n, count the number of unique paths from top-left to bottom-right, moving only right or down

function countPaths(m, n) {
  // base case - only 1 path if m or n is 1
  if (m  === 1 || n === 1) return 1;

  return countPaths(m-1, n) + countPaths(m, n-1);
}

function countPaths(m, n, memo = {}) {
  // base case - only 1 path if m or n is 1
  if (m  === 1 || n === 1) return 1;

  const key = `${m}, ${n}`;

  if (memo[key]) return memo[key];
  memo[key] = countPaths(m-1, n) + countPaths(m, n-1);

  return memo[key];
}

function lengthOfLongestSubstring(str) {
  let maxLen = 0;
  let start = 0;
  let lastSeen = {};

  for (let end = 0; end < str.length; end ++) {
    const char = str[end];

    if (char in lastSeen && lastSeen[char] >= start) {
      start = lastSeen[char] + 1;
    }
    lastSeen[char] = end;
    maxLen = Math.max(maxLen, end - start + 1);
  }

  return maxLen;
}

// console.log(lengthOfLongestSubstring("pbbabcbcbb"))
```

### Frequency Counting
- good for comparison, duplicates, patterns in data

```javascript
function areAnagrams(str1, str2) {
  if (str1.length !== str2.length) return false;

  const frequency = {};

  for (const char of str1) {
    frequency[char] = (frequency[char] || 0) + 1;
  }

  for (const char of str2) {
    if (!frequency[char]) return false;
    frequency[char]--;
  }

  return true;
}
```

### Multiple Pointers
- use 2 or more pointers to keep track of position
- update the pointer positions

```javascript
function findPairWithSum(arr, target) {
  let left = 0;
  let right = arr.length - 1;

  while (left < right) {
    const sum = arr[left] + arr[right];

    if (sum === target) {
      return [arr[left], arr[right]];
    }
    if (sum < target) {
      left++
    }
    if (sum > target) {
      right--;
    }
  }

  return null;
}

// find a pair of numbers that add up to a target number
// arr = [1,2,4,6,8,8,9], target = 12
// pair = [4,8]
```

### Sliding Windows
- use a "window" that "slides" across your data

```javascript
// Given an array of integers and a number k, find the max sum of a contiguous subarray of size k

function maxSubarraySum(arr, k) {
  if (arr.length < k) return null;
  
  let sum = 0;
  let max = 0;

  // first window sum
  for (let i = 0; i < k, i++) {
    sum += arr[i];
  }
  max = sum;

  // slide window over array
  for (let i = k; i < arr.length; i++) {
    sum += arr[i] - arr[i-k]; // add tail and remove head
    max = Math.max(max, sum);
  }

  return max;
}
```