Student Info

Name: Krishnaveno

Registration Number: 171

Course: Data Structures Assignment – September 2025

1: Stack and Queue

Stack

Files in Repo:

Stack_Using_Arrays.py → Stack using fixed-size array

Stack_Using_LinkedList.py → Stack using linked list

Operations Implemented:

push() – Insert element

pop() – Remove top element

peek() – View top element

isEmpty() – Check if stack is empty

display() – Show elements

Queue

Files in Repo:

Queue_Using_Arrays.py → Queue using circular array

Queue_using_LinkedList.py → Queue using linked list

Operations Implemented:

enqueue() – Insert element at rear

dequeue() – Remove element from front

front() – View front element

isEmpty() – Check if queue is empty

display() – Show elements

 2: Binary Search Tree (BST)

File in Repo:Binary Search Tree.py

Features Implemented:

Insertion

Searching

Traversals: In-order, Pre-order, Post-order

Bonus: Deletion of nodes

Task 3: Sorting and Searching

Sorting

Files in Repo:

Bubble Sort.py – Bubble Sort

Merge Sort.py – Merge Sort

QuickSort.py – Quick Sort

Searching

Files in Repo:

Linear Search.py – Linear Search

Binary Search.py – Binary Search (iterative + recursive inside one file)

How to Run

Clone the repository:https://github.com/krishnaveni1709/BT-DATASTRUCTURES-SEP-2025-171

git clone 

cd DS-SEP-2025-171

Run any program file individually, for example:

python Stack_Using_array.py

python queue_Using_LinkedList.py

python bst.py

python Bubble sort.py

python Linear search.py

Example Outputs:

👉 Stack (Array Implementation):

Stack elements: [10, 20, 30]

Top element: 30

Stack elements: [10, 20]

Top element: 20

Is stack empty? False

👉 Stack (Linked List Implementation):

Stack is empty

30->20->10->None

Popped: 30

Peek: 20

20->10->None

👉 Queue (Array Implementation):

Enqueued 30

Enqueued 50

Enqueued 9

Queue elements: 30 50 9

Dequeued 30

front element 50

Queue elements: 50 9

👉 Queue (Linked List Implementation):

Enqueued 10

Enqueued 20

Enqueued 30

Queue elements: 10 20 30

Dequeued 10

Front element: 20

Queue elements: 20 30

👉 BST:

Preorder:3 5 4 6 7 8 12 45

postorder:4 45 12 8 7 6 5 3

inorder:3 4 5 6 7 8 12 45

levelorder:[3, 5, 4, 6, 7, 8, 12, 45]

Inorder traversal after deleting 6:3 4 5 7 8 12 45

Inorder Traversal after updating 3 to 5:4 5 7 8 12 45

True

True

True

True

👉 Sorting:

Original: [5, 2, 9, 1, 6]

Bubble Sort: [1, 2, 5, 6, 9]

Merge Sort: [1, 2, 5, 6, 9]

Quick Sort: [1, 2, 5, 6, 9]

👉 Searching:

Array: [2, 4, 6, 8, 10]

Linear Search (8): Found at index 3

Binary Search (8): Found at index 3

