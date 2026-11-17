# https://github.com/kou229/AtCoder
import sys
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
from itertools import accumulate, permutations, combinations, product
from functools import lru_cache
from math import gcd, inf

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# 整数を1つ読む
#   入力: 5        → n = I()
def I():
    return int(input())


# 1行の整数をばらして受け取る（アンパック専用。a[0] のようには使えない）
#   入力: 3 4      → n, m = MI()
def MI():
    return map(int, input().split())


# 1行の整数をリストで受け取る
#   入力: 1 2 3    → a = LI()
#   N 行あるとき  → a = [LI() for _ in range(n)]
def LI():
    return list(map(int, input().split()))


# 文字列を1つ読む（末尾の改行を取り除く）
#   入力: abc      → s = S()
def S():
    return input().rstrip("\n")


# ここに解答を書く（関数の中の方がグローバルより速い）
def main():
    n, q = MI()
    k = LI()
    a = [0] * n
    for i in range(n):
        a[i] = i + 1

    for i in range(q):
        temp = [0] * k[i]
        for j in range(k[i]):
            temp[j] = -1 * a[k[i] - 1 - j]
        for j in range(k[i]):
            a[j] = temp[j]

  
    print("\n".join(map(str, a)))


main()
