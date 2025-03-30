## Search Algo
### Binary Search
- Can only be used when the data is sorted

```javascript
function bSRecursive(arr, value, left = 0, right = arr.length - 1) {
  // base case: either find the value or determine it's not in the array
  if (left > right) return -1;

  let middle = Math.floor((left + right) / 2);
  
  if (arr[middle] === value) return middle; // index of the value
  if (arr[middle] < value) return bSRecursive(arr, value, middle + 1, right);
  if (arr[middle] > value) return bSRecursive(arr, value, left, middle - 1);
}
```

### Additional
```javascript
function linearSearch(arr, num) {
  for (let i = 0; i < arr.length; i++)  {
    if (arr[i] === num) return i;
  }
  return -1;
}

linearSearch([1, 2, 3, 4, 5], 3); // Output: 2

function binarySearch(arr, value) { // O(log n)
  let left = 0;
  let right = arr.length - 1;

  while (left <= right) {
    let middle = Math.floor((left + right) / 2);

    if (arr[middle] === value) return middle;
    if (arr[middle] < value) left = middle + 1;
    if (arr[middle] > value) right = middle - 1;
  }

  return -1;
}

binarySearch([1,2,4,5,6,7,9,10,11,12], 4); // Output: 2
```