# ============================================================================
# DECISION TREES FOR BACKTRACKING — draw them fast in an interview
# ============================================================================
#
# RECIPE (answer these; the tree draws itself):
#   1. NODE   = the STATE   -> "where am I?"
#   2. BRANCH = the CHOICES -> what can I do here?        (edges, labeled)
#   3. PRUNE  = illegal/hopeless branch -> cut it  X      (cut the BRANCH on a path, not the element)
#   4. LEAF   = OK goal reached  |  XX dead-end -> backtrack
#   5. LEAF ACTION -> what the question wants (this alone separates variants):
#        "possible?"  -> return True on FIRST OK   (can stop early)
#        "how many?"  -> COUNT OK leaves           (must walk whole tree)
#        "list them?" -> APPEND a copy per OK leaf (must walk whole tree)
#        "max / min?" -> track BEST over OK leaves (must walk whole tree)
#
# DRAWING DISCIPLINE (~30s, not the whole tree):
#   root + branches, ONE path to OK, ONE path to XX, a couple X siblings, "..."
#   The tree is the SEARCH; most leaves fail — normal.
#
#
# ============================================================================
# P1 — N-QUEENS
# ============================================================================
# Place n queens on an n*n board so that no two share a row, column, or
# diagonal. Find all valid arrangements.
#
# Hinge: one queen per row -> fill row by row, only choice is "which column".
#   NODE=row r | BRANCH=column 0..n-1 | PRUNE=same col or |dr|==|dc| X
#   LEAF: r==n -> OK  /  no legal col -> XX
#
#   row0:                *
#             c0/   c1|   c2|   c3\
#   row1:     c2     c3     c0    (mirror of c0)
#              |      |      |
#   row2:     XX     c0     c3          under c1: row1 cols c0/c1/c2 pruned X,
#          dead      |      |           only c3 survived
#   row3:           c2     c1
#                   OK      OK
#                [1,3,0,2][2,0,3,1]     the two are mirrors: c -> (n-1-c)
#
#
# ============================================================================
# P2 — SUBSET SUM TO ZERO
# ============================================================================
# Given an array of unique integers and a positive k, is there a subset of
# exactly k elements that adds up to 0?  (framing: include/exclude each element)
#
#   NODE=(i,count,sum) | BRANCH=take arr[i] / skip arr[i]
#   PRUNE=count>k X (also count+left<k) | LEAF: count==k -> check sum==0
#
#   arr=[-1,1,2], k=2   (node=(count,sum); T=take S=skip)
#                          (0,0) decide -1
#                    T /                    \ S
#               (1,-1) dec 1             (0,0) dec 1
#              T /      \ S              T /      \ S
#         (2,0) OK    (1,-1) dec 2   (1,1) dec 2  (0,0) dec 2
#         {-1,1}      T/    \S        T/   \S      T/    \S
#         sum=0     (2,1) (1,-1)   (2,3)(1,1)   (1,2) (0,0)
#                   fail  fail     fail fail    fail  fail
#   Note: under (2,0) count==k, so "decide 2" is pruned there — but 2 is still
#   TAKEN on other paths. Cut the BRANCH, not the element.
#
#
# ============================================================================
# P3 — GRAPH k-COLORING
# ============================================================================
# Given an undirected connected graph and k colors, can every node be colored
# so that adjacent nodes always differ? (non-adjacent nodes may share a color.)
#
# Same tree as N-Queens, renamed: row->node, column->color,
#   "col attacked"->"neighbor already has this color".
#   NODE=node i | BRANCH=color 0..k-1 | PRUNE=neighbor uses it X
#   LEAF: all colored -> OK  /  no legal color -> XX
#
# Triangle A-B-C (all adjacent), order A->B->C.
#
# k=2 (colors R,B) -> IMPOSSIBLE (zero OK leaves = "no"):
#            *
#        R /   \ B
#        A=R    A=B
#         |      |          A=R forces B=B; then C touches both -> both
#        B=B    B=R         colors pruned -> XX. A=B is the mirror. No OK leaf.
#         |      |
#        XX      XX
#
# k=3 (colors R,G,B) -> POSSIBLE. Count = OK leaves = 3*2*1 = 6:
#   A:3 choices -> B:2 (!=A) -> C:1 (!=A,B)
#   RGB RBG  GRB GBR  BRG BGR
#   "possible?" -> True.   "how many?" -> 6.   (same tree, different leaf action)
#
#
# ============================================================================
# P4 — MAX-SUM PATH, 4 DIRECTIONS, NO REVISIT
# ============================================================================
# Given an R*C grid of positive AND negative integers, find the path from the
# top-left to the bottom-right cell that maximizes the sum. You may move up,
# down, left, or right (no diagonals) and cannot visit a cell more than once.
#
# Backtracking not DP: visited set is part of the state -> subproblems don't
# overlap -> no memo. (P39.1 down/right-only has no visited set -> DP.)
#
#   NODE=(cell (r,c), visited set, running sum)
#   BRANCH=4 neighbors: up / down / left / right
#   PRUNE=neighbor out of bounds  X   or already visited  X
#   LEAF=reached bottom-right (R-1,C-1) -> OK      ACTION=keep the MAX sum
#
# GOTCHA: leaf = reach the target, NOT "visit every cell"; no-revisit is a PRUNE.
#
# grid = [[ 1, -2],
#         [ 3,  4]]   start (0,0), goal (1,1); node=(cell,sum); up/left = oob X
#
#                    (0,0) sum=1
#          up X   down|       right\   left X
#                (1,0) sum=4      (0,1) sum=-1
#                    |               |
#                 right            down
#                    |               |
#                (1,1) sum=8      (1,1) sum=3
#                   OK               OK
#                    \______ max ____/
#                          = 8
