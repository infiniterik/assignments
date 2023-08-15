# CS 205: Algorithm design and analysis Fall Term, 2022
## Homework 2

### 1. AVL Tree Insertion

To draw the result of adding the given values to an initially empty AVL tree, we will follow the steps of AVL tree insertion and rebalancing after each operation. The values will be added one at a time in the given order.

#### Step 1: Insert 205
```
     205
```
The tree is balanced after inserting 205.

#### Step 2: Insert 309
```
     205
       \
        309
```
The tree is balanced after inserting 309.

#### Step 3: Insert 330
```
     205
       \
        309
          \
           330
```
The tree is balanced after inserting 330.

#### Step 4: Insert 142
```
     205
    /   \
  142    309
          \
           330
```
The tree is balanced after inserting 142.

#### Step 5: Insert 141
```
     205
    /   \
  142    309
  /
141
```
The tree is unbalanced after inserting 141. We need to perform a left rotation.

#### Step 6: Left rotation after inserting 141
```
     205
    /   \
  141    309
  /
142
```
The tree is balanced after the left rotation.

#### Step 7: Insert 214
```
     205
    /   \
  141    309
  / \
142  214
```
The tree is balanced after inserting 214.

#### Step 8: Insert 220
```
     205
    /   \
  141    309
  / \
142  214
      \
      220
```
The tree is balanced after inserting 220.

#### Step 9: Insert 208
```
     205
    /   \
  141    309
  / \
142  214
  \   \
  208 220
```
The tree is balanced after inserting 208.

### 2. Proof by Induction

To prove the identity using induction, we will follow the steps below:

**Base Case:** For n = 1,
```
1/(1x3) = 1/3
```
```
n/(2n+1) = 1/(2+1) = 1/3
```
The base case holds true.

**Inductive Step:** Assume the identity holds for n = k, where k >= 1.

We need to prove that the identity holds for n = k+1.

```
1/(1x3) + 1/(3x5) + 1/(5x7) + ... + 1/((2k-1)(2k+1)) + 1/((2(k+1)-1)(2(k+1)+1))
```
```
= k/(2k+1) + 1/((2(k+1)-1)(2(k+1)+1))
```
```
= k/(2k+1) + 1/((2k+1+1)(2k+1+1))
```
```
= k/(2k+1) + 1/((2k+2)(2k+2))
```
```
= k/(2k+1) + 1/(4k^2 + 8k + 4)
```
```
= (k(4k^2 + 8k + 4) + 1(2k+1))/(2k+1)(4k^2 + 8k + 4)
```
```
= (4k^3 + 8k^2 + 4k + 2k + 1)/(2k+1)(4k^2 + 8k + 4)
```
```
= (4k^3 + 8k^2 + 6k + 1)/(2k+1)(4k^2 + 8k + 4)
```
```
= (2k+1)(2k+1)/(2k+1)(4k^2 + 8k + 4)
```
```
= (2k+1)/(4k^2 + 8k + 4)
```
```
= (k+1)/(2(k+1)+1)
```
```
= (k+1)/(2k+3)
```

Therefore, the identity holds for n = k+1.

By the principle of mathematical induction, the identity holds for all positive integers n.

### 3. Case 2a of AVL Tree Restoration Proof

In case 2a of the proof that the algorithm from class restores the AVL tree property, we assume that the imbalance occurs in the left subtree of the left child of the node being inserted.

**Step 1:** Let's assume the node being inserted is X, and the left child of X is Y.

**Step 2:** The imbalance occurs when the height of the left subtree of Y is greater than the height of the right subtree of Y.

**Step 3:** We need to perform a right rotation on Y.

**Step 4:** After the right rotation, the left subtree of Y becomes the right subtree of X, and the right subtree of the left child of Y becomes the left subtree of Y.

**Step 5:** The heights of the left and right subtrees of X are updated accordingly.

**Step 6:** The AVL tree property is restored.

Justification for Step 3: A right rotation on Y is performed to balance the tree and restore the AVL property. This rotation ensures that the height of the left subtree of Y is reduced by one, while the height of the right subtree of Y remains the same or increases by one.

Justification for Step 4: After the right rotation, the left subtree of Y becomes the right subtree of X, and the right subtree of the left child of Y becomes the left subtree of Y. This rearrangement maintains the order of the elements in the tree.

Justification for Step 5: The heights of the left and right subtrees of X are updated based on the heights of the corresponding subtrees before the rotation. The height of the left subtree of X is reduced by one, while the height of the right subtree of X remains the same or increases by one.

Justification for Step 6: By performing the right rotation, the AVL tree property is restored as the heights of the left and right subtrees of each node are balanced, and the difference in heights is at most 1.

This completes the justification for case 2a of the proof that the algorithm from class restores the AVL tree property.