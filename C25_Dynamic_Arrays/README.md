# Why append's amortized time is O(1)?
If you do n appends total, and the total work done by all the resize operations combined is O(n), the average work per append operation is:

Total work = O(n), divided by n operations 
  = O(n) / n
  = O(1)
So the amortized time complexity of append is O(1), not O(log n).

This is a key insight - even though individual appends might take O(n) time when resizing happens, the average time per append across many operations is still constant.

# Why the overall space complexity is O(n)? It can have many extra None taking up spaces
You use at most 2n space total (n for actual elements, n for unused slots). Since 2n is still O(n), the space complexity is O(n).
