
This program implements the ArrayList data structure.

I use an array on the heap to store data. We keep track of the size and capacity
of the array using two private variables (size and capacity). This ensures that
other's won't accidentally change them.

Resize is needed when
1) the size is over 3/4 of the capacity so the index is never out of the range
2) the size is below 1/4 of the capacity to save memory space
Resize is a private function for implemention hidden prupose.
To resize the array, we first create a new array on the heap of desired length
and then copy everything from the old array to this new array
finally delete the old array and set the pointer to the new array.

The only two cases when we need to consider about the issue of resize is when we use
insert and remove function since these are the only cases when array size will change

getSize() and getCapacity() are functions that grant user the ability
to check current size and capaccibility

find(int x) and elementAt(int x) granys extra functionality
,tells the user whether x is in the array and returns the interger at index x respectively.

