## Sorting Algo
### Bubble Sort
- Time Complexity: O(n)
- Space Complexity: O(1)
- Iterates the data and compares adjacent values, starting at index 0
- The values are swapped if the first is larger than the second
- The largest number bubbles to the end. Then starts again from the beginning

```javascript
function bubbleSort(arr) {
  for (let i = arr.length - 1; i > 0; i--) {
    let swap = false;

    for (let j = 0; j < i; j++) {
      if (arr[j] > arr[j + 1]) {
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
        swap = true;
      }
    }

    if (!swap) break;
  }

  return arr;
}
```

### Selection Sort
- Time Complexity: O(n^2)
- Space Complexity: O(1)
- Find the smallest value in the unsorted portion and move it to the correct position

```javascript
function selectionSort(arr) {
  for (i = 0; i < arr.lenght - 1; i++) {
    let index = i;

    for (let j = i + 1; j < arr.length; j++) {
      if (arr[j] < arr[index]) index = j;
    }

    if (index !== i) {
      [arr[i], arr[index]] = [arr[index], arr[i]];
    }
  }

  return arr;               
}
```

### Merge Sort
- Time Complexity: O(n log n), Loglinear time
- Space Complexity: O(n)
- Split the array into smaller arrays
- Merge those smaller arrays back together in the correct order

- Why O(n log n) Time?
At each level of recursion, the array is split in half (log n levels).
At each level, all n elements are merged.
So, total work = n (per level) × log n (levels) = O(n log n), 

- Why O(n) Space?
Each merge operation requires a temporary array to store the merged result, which can be up to the size of the original array, so O(n) extra space is needed

```javascript
// a helper function to merge two sorted arrays
function mergeTwoArrays(arrOne, arrTwo) {
  let totalLength = arrOne.length + arrTwo.length
  let merged = [];
  let i = 0; 
  let j = 0;

  while (merged.length < totalLength) {
    if (i >= arrOne.length) { // no more value in arrOne
      merged.push(arrTwo[j]);
      j++;
      continue;
    }

    if (j >= arrTwo.length) { // no more value in arrTwo
      merged.push(arrOne[i]);
      i++;
      continue;
    }

    if (arrOne[i] <= arrTwo[j]) { // ele in arrOne is smaller
      merged.push(arrOne[i]);
      i++;
      continue;
    }

    merged.push(arrTwo[j]); // ele in arrTwo is smaller
    j++;
  }

  return merged;
}

function mergeSort(arr) {
  // base case - return array if length <= 1 (already sorted)
  if (arr.length <= 1) return arr;

  let middle = Math.floor(arr.length / 2);

  // resursive calls
  let left = mergeSort(arr.slice(0, middle));
  let right = mergeSort(arr.slice(middle));

  return mergeTwoArrays(left, right);
}

// input: [9,2,5,4]
//  --> left = mergeSort([9,2]) & right mergeSort([5,2])
//  --> return mergeTwoArrays([2,9], [4,5]) = [2,4,5,9]

  // input: [9,2]
  //  --> left = mergeSort([9]) & right = mergeSort([2])
  //  --> left = [9] & right = [2]
  //  --> return mergeTwoArrays([9], [2]) = [2,9]

  // input: [5,4]
  //  --> left = mergeSort([5]) & right = mergeSort([4])
  //  --> left = [5] & right = [4]
  //  --> return mergeTwoArrays([5], [4]) = [4,5]
```