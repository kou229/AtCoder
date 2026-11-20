# AWC0204 振り返り

https://atcoder.jp/contests/awc0204

| 問題 | 結果 | 難易度の目安（推定） | ポイント |
| --- | --- | --- | --- |
| A | 自力 AC | 灰 | 文字列に `x` が含まれるか |
| B | 自力 AC | 灰 | 最初の `z` の位置 |
| C | 自力 AC | 茶 | 「値ごとの個数」で持つ |
| D | 自力 AC | 緑（800〜1000） | DP の遷移を累積 min でまとめる |
| E | 未 AC | 水（1200〜1400） | 偶奇付き Union-Find ＋ 偶奇 DP |

※ AWC は AtCoder Problems に難易度が出ていないので、目安は推定。

---

## A. Does the Current Flow?

自分の解答：`"x" in s` で判定。**これがベスト**。直すところなし。

---

## B. The First Nap

自分の解答：for で 1 文字ずつ見て、最初の `z` で `print(i + 1)` して `return`。正しい。

改善案：`str.find` を使うと 1 行で書ける。見つからないときは `-1` が返る。

```python
i = s.find("z")
print(i + 1 if i >= 0 else -1)
```

---

## C. Price Revision

自分の解答：`defaultdict` で「価格 → その価格の商品の個数」を持ち、操作ごとに
`総和 += (C - B) × 個数` で更新。**考え方はこれが想定解**（1 回あたり O(1)、全体で O(N + Q)）。

改善案：

1. **出力はまとめて出す**
   Q = 10^5 回 `print` するのは遅めなので、リストにためて最後に 1 回で出力する。
   今回は間に合うが、出力が 10^5 行を超える問題では差が出る。
2. **書き方を短くする**
   - 総和は `sum(a)`、個数は `Counter(a)` で作れる。
   - `bc[i][0]` のように添字で取るより、`for b, c in bc:` で取り出すと読みやすい。
3. **値の範囲が小さいときは配列で持つ**
   値は 10^5 以下なので、`cnt = [0] * (10**5 + 1)` の配列でもよい。dict より速い。

```python
def main():
    n = I()
    a = LI()
    q = I()
    cnt = Counter(a)
    total = sum(a)
    out = []
    for _ in range(q):
        b, c = MI()
        k = cnt[b]
        total += (c - b) * k
        cnt[b] = 0
        cnt[c] += k
        out.append(total)
    print("\n".join(map(str, out)))
```

> `cnt[b] = 0` を `cnt[c] += k` より先にしているが、B ≠ C が保証されているのでこの順番でも問題ない。
> B = C がありえる問題なら、先に足してから消すと消えてしまうので注意。

---

## D. Heights of Display Stands and Production Costs

自分の解答：`saiyasune[i][j]` を「展示台 i の高さを **j 以下** にしたときの最小料金」と定義して、

```
saiyasune[i][j] = min(saiyasune[i-1][j] + c[i][j],  saiyasune[i][j-1])
                     （高さをちょうど j にする）     （高さを j-1 以下にする）
```

**これは良い定義**。「高さがちょうど j」で定義すると `min(dp[i-1][0..j])` が必要になるが、
「j 以下」で定義すると累積 min が DP の中に入るので、別に累積 min を取る必要がない。

改善案：

1. **1 次元の配列で回す**
   使うのは 1 つ前の行だけなので、配列を 1 本にして上書きしていける。メモリは N×M → M。
2. **i = 0 と j = 0 の場合分けを消す**
   - `dp` の初期値を `[0] * m`（展示台が 0 台なら料金 0）にすると、i = 0 も同じ式で計算できる。
   - 左側の最小値 `best` の初期値を `inf` にすると、j = 0 も同じ式で計算できる。
3. **答えは `dp[-1]`**
   「j 以下」の定義なので、最後の要素が全体の最小値になる（`min()` を取らなくてよい）。

```python
def main():
    n, m = MI()
    dp = [0] * m          # dp[j] = 高さを j 以下にしたときの最小料金
    for _ in range(n):
        row = LI()
        best = inf
        for j in range(m):
            v = dp[j] + row[j]
            if v < best:
                best = v
            dp[j] = best
    print(dp[-1])
```

N = M = 2000 の最大ケース（CPython）で、元の解答が約 1.0 秒、上のコードが約 0.6 秒だった。
どちらも制限時間内に収まる。

---

## E. Grid Changed by an Even Number of Switches

### 問題の要約

- H × W の盤面で、初めはすべて白。行 r のスイッチを押すとその行が反転し（費用 A_r）、列 c のスイッチを押すとその列が反転する（費用 B_c）。
- 各スイッチは高々 1 回まで押せて、**押す個数の合計は偶数**でなければならない。
- 「マス (r, c) の最終的な色は t」という条件が M 個あり、すべて満たすときの最小費用を求める（できなければ -1）。

### 考え方

**1. 条件を式に直す**

行 r を押すなら x_r = 1、押さないなら x_r = 0 とし、列 c についても同じように y_c と書く。
マス (r, c) は行と列で合わせて x_r + y_c 回反転するので、最終的な色は `x_r xor y_c`。
したがって条件 i は

```
x_{r_i} xor y_{c_i} = t_i
```

になる。押す順番は結果に関係しない。

**2. グラフにする**

行 H 個と列 W 個を頂点にして、条件ごとに「行 r と列 c は、t = 0 なら同じ値、t = 1 なら違う値」という辺を張る。
これは「偶奇付き Union-Find」（重み付き Union-Find の xor 版）で扱える。

- 同じ連結成分にある 2 頂点の関係（同じ値か違う値か）は、条件から一通りに決まる。
- 条件が矛盾したら（同じ成分の中で関係が食い違ったら）-1。

**3. 連結成分ごとに 2 択**

ひとつの連結成分の中では、1 頂点の値を決めると残りがすべて決まる。
したがって、各成分の選び方は次の 2 通りしかない。

- 案 0：根を押さない → 根と値が違う頂点だけを押す
- 案 1：根を押す → 案 0 で押した頂点と押さなかった頂点が入れ替わる

それぞれについて (費用, 押す個数) を計算しておく。
条件が 1 つも付いていない行や列は 1 頂点だけの成分で、(0, 0 個) か (A_r, 1 個) の 2 択になる。

**4. 個数の偶奇を DP で合わせる**

成分ごとの 2 択は独立だが、「合計の個数が偶数」という制約が全体にかかる。そこで

```
dp[p] = ここまでの成分で、押した個数の偶奇が p のときの最小費用
```

を持って成分を 1 つずつ足していく。最後に残った `dp[0]` が答え。

計算量は、Union-Find がほぼ O(M)、DP が O(H + W) で、全体でほぼ O(H + W + M)。

### 実装のポイント

- 頂点番号は、行を `0..H-1`、列を `H..H+W-1` にまとめる。
- `par[v]` = 「v の値 xor 親の値」。`find` のときに根までの xor を足し込みながら経路を縮める。
- 再帰で書くと深くなるので、ループで書く（PyPy でも安全）。
- 2 つの成分をつなぐときは、`par[根a] = par[a] ^ par[b] ^ t` にすると a と b の関係が t になる。

### 解答コード

```python
import sys


def main():
    data = sys.stdin.buffer.read().split()
    H, W, M = int(data[0]), int(data[1]), int(data[2])
    cost = [int(x) for x in data[3:3 + H + W]]  # 0..H-1 が行、H..H+W-1 が列
    N = H + W

    parent = list(range(N))
    par = [0] * N  # 親に対する偶奇（自分 xor 親）

    def find(x):
        # 根までたどりながら経路圧縮し、根に対する偶奇も更新する
        path = []
        while parent[x] != x:
            path.append(x)
            x = parent[x]
        root = x
        acc = 0
        for v in reversed(path):
            acc ^= par[v]
            par[v] = acc
            parent[v] = root
        return root

    idx = 3 + H + W
    for _ in range(M):
        r = int(data[idx]) - 1
        c = H + int(data[idx + 1]) - 1
        t = int(data[idx + 2])
        idx += 3
        ra, rb = find(r), find(c)
        if ra == rb:
            if par[r] ^ par[c] != t:
                print(-1)
                return
        else:
            parent[ra] = rb
            par[ra] = par[r] ^ par[c] ^ t

    # 成分ごとに「根を押さない」とした場合の (費用, 個数) と成分全体の (費用, 個数)
    on_cost = [0] * N
    on_cnt = [0] * N
    all_cost = [0] * N
    all_cnt = [0] * N
    for v in range(N):
        root = find(v)
        all_cost[root] += cost[v]
        all_cnt[root] += 1
        if par[v]:
            on_cost[root] += cost[v]
            on_cnt[root] += 1

    INF = float("inf")
    dp = [0, INF]  # dp[p] = 押した個数の偶奇が p のときの最小費用
    for v in range(N):
        if parent[v] != v:
            continue
        c0, k0 = on_cost[v], on_cnt[v] & 1
        c1, k1 = all_cost[v] - on_cost[v], (all_cnt[v] - on_cnt[v]) & 1
        ndp = [INF, INF]
        for p in range(2):
            if dp[p] == INF:
                continue
            ndp[p ^ k0] = min(ndp[p ^ k0], dp[p] + c0)
            ndp[p ^ k1] = min(ndp[p ^ k1], dp[p] + c1)
        dp = ndp

    print(dp[0] if dp[0] != INF else -1)


main()
```

サンプル 5 つで一致。さらに、小さいケース 500 個をランダムに作って全探索の結果と比べ、すべて一致した。

### 学んだこと

- 「2 つの値が同じか違うか」という条件が並んだら、**偶奇付き Union-Find**（または BFS で 2 色に塗る）。
- 連結成分ごとに選び方が 2 通りしかないときは、**成分ごとの 2 択を DP でまとめる**。今回の偶奇の制約のように、全体にかかる制約は DP の状態に入れる。
- 似た典型：ABC 087 D「People on a Line」（重み付き Union-Find）、ABC 126 E「1 or 2」。
