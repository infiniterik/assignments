# Ask
The assignment is asking for the following:

1. Draw the result of adding the given values to an initially empty AVL tree, one at a time in the given order. Show the balanced tree after each insertion, including any necessary rebalancing operations.

2. Use induction to prove the identity: 1/(1x3)+1/(3x5)+1/(5x7)+...+ 1/((2n-1)(2n+1)) = n/(2n+1).

3. Complete case 2a of the proof that the algorithm from class restores the AVL tree property. Provide justifications for each step.

# Answer

# CS 205: Algorithm design and analysis Fall Term, 2022
## Homework 2

**Due: Friday 9/23 at 11:59pm**

---

## Problem 1: AVL Tree Insertion

### Task
Draw the result of adding the following values to an initially empty AVL tree: 205, 309, 330, 142, 141, 214, 220, and 208. These values should be added one at a time in the given order. Rebalancing operations are part of the insertion, so the tree should be rebalanced after each operation. Show the balanced tree after each insertion (8 figures) at a minimum; you may also show the tree before the rotations if you wish.

### Solution

1. Inserting 205:
   ```
         205
   ```

2. Inserting 309:
   ```
         205
          \
           309
   ```

3. Inserting 330:
   ```
         205
          \
           309
             \
              330
   ```

4. Inserting 142:
   ```
         205
        /   \
      142    309
              \
               330
   ```

5. Inserting 141:
   ```
         205
        /   \
      142    309
     /
   141
              \
               330
   ```

6. Inserting 214:
   ```
         205
        /   \
      142    309
     /  \
   141   214
              \
               330
   ```

7. Inserting 220:
   ```
         205
        /   \
      142    309
     /  \     \
   141   214   330
              /
            220
   ```

8. Inserting 208:
   ```
         205
        /   \
      142    309
     /  \     \
   141   208   330
          \    /
          214 220
   ```

---

## Problem 2: Induction Proof

### Task
Use induction to prove the following identity: 1/(1x3)+1/(3x5)+1/(5x7)+...+ 1/((2n-1)(2n+1)) = n/(2n+1).

### Solution

**Base Case:**
For n = 1, the left-hand side (LHS) of the equation is:
LHS = 1/(1x3) = 1/3

The right-hand side (RHS) of the equation is:
RHS = 1/(2(1)+1) = 1/3

Therefore, the equation holds true for n = 1.

**Inductive Step:**
Assume that the equation holds true for n = k, i.e.,

1/(1x3)+1/(3x5)+1/(5x7)+...+ 1/((2k-1)(2k+1)) = k/(2k+1)

We need to prove that the equation holds true for n = k+1, i.e.,

1/(1x3)+1/(3x5)+1/(5x7)+...+ 1/((2k-1)(2k+1)) + 1/((2(k+1)-1)(2(k+1)+1)) = (k+1)/(2(k+1)+1)

Adding the next term to both sides of the equation:

LHS + 1/((2(k+1)-1)(2(k+1)+1)) = RHS + 1/((2(k+1)-1)(2(k+1)+1))

Substituting the assumption:

(k/(2k+1)) + 1/((2(k+1)-1)(2(k+1)+1)) = (k+1)/(2(k+1)+1)

Multiplying both sides by (2k+1)(2(k+1)+1):

k(2(k+1)+1) + 1 = (k+1)(2k+1)

Expanding and simplifying:

2k^2 + 3k + 1 = 2k^2 + 3k + 1

Therefore, the equation holds true for n = k+1.

By the principle of mathematical induction, the equation holds true for all positive integers n.

---

## Problem 3: AVL Tree Property Restoration

### Task
Complete case 2a of the proof that the algorithm from class restores the AVL tree property. Provide justifications for each step.

### Solution

**Case 2a:**
Suppose the left subtree of node A is higher than the right subtree, and the left subtree of node B is higher than the right subtree.

```
        A
       / \
      B   C
     / \
    D   E
```

To restore the AVL tree property, we need to perform a right rotation on node A.

```
        B
       / \
      D   A
         / \
        E   C
```

Justifications:
1. The left subtree of node A is higher than the right subtree, so we perform a right rotation on node A to balance the tree.
2. The left subtree of node B is higher than the right subtree, so we perform a right rotation on node B to balance the tree.
3. The tree is now balanced, and the AVL tree property is restored.