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


# 整数の行を n 行読んで、行ごとのリストで受け取る
#   入力: N M のあとに A_i B_i が M 行
#     n, m = MI()
#     ab = LLI(m)              → ab = [[A1, B1], [A2, B2], ...]
#     for a, b in ab: ...      → 1行ずつ取り出す
#     A, B = map(list, zip(*ab))  → 列ごとに分ける（A = [A1, A2, ...]）※ m = 0 だと使えない
def LLI(n):
    return [list(map(int, input().split())) for _ in range(n)]


# 文字列を1つ読む（末尾の改行を取り除く）
#   入力: abc      → s = S()
def S():
    return input().rstrip("\n")


# ここに解答を書く（関数の中の方がグローバルより速い）
def main():
    pass


main()
