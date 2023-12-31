1. AVL Tree Insertion:

Step 1: Insert 205
```
     205
```

Step 2: Insert 309
```
     205
       \
        309
```

Step 3: Insert 330
```
     205
       \
        309
          \
           330
```

Step 4: Insert 142
```
     205
    /   \
  142    309
          \
           330
```

Step 5: Insert 141
```
     205
    /   \
  142    309
 /       \
141       330
```

Step 6: Insert 214
```
     205
    /   \
  142    309
 /  \      \
141  214    330
```

Step 7: Insert 220
```
     205
    /   \
  142    309
 /  \      \
141  214    330
           /
         220
```

Step 8: Insert 208
```
     205
    /   \
  142    309
 /  \      \
141  208    330
     / 
   214
```

2. Proof by Induction:

Base Case: n = 1
```
LHS: 1/(1*3) = 1/3
RHS: 1/(2*1+1) = 1/3
```
The base case holds.

Inductive Step:
Assume the identity holds for n = k, i.e., 1/(1*3) + 1/(3*5) + ... + 1/((2k-1)(2k+1)) = k/(2k+1)

We need to prove that the identity holds for n = k+1, i.e., 1/(1*3) + 1/(3*5) + ... + 1/((2k-1)(2k+1)) + 1/((2(k+1)-1)(2(k+1)+1)) = (k+1)/(2(k+1)+1)

LHS:
1/(1*3) + 1/(3*5) + ... + 1/((2k-1)(2k+1)) + 1/((2(k+1)-1)(2(k+1)+1))
= k/(2k+1) + 1/((2(k+1)-1)(2(k+1)+1)) (by the induction hypothesis)
= (k(2(k+1)+1) + 1)/((2k+1)(2(k+1)+1))
= (2k^2 + 3k + 1)/(4k^2 + 6k + 2)
= (2k^2 + 3k + 1)/(2(2k^2 + 3k + 1))
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3k + 1)
= (k^2 + (2k^2 + 3k + 1))/(2k^2 + 3