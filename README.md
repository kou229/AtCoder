# AtCoder

## 構成
```
AtCoder/
├── python/
│   ├── template.py      ← 新しい問題ファイルの雛形（入力の関数、よく使う import）
│   └── lib/             ← 自作ライブラリ（Union-Find など）
├── contests/<contest>/  ← コンテストごと（abc400/a.py ... g.py, tests/<問題>/sample-N.in/.out）
├── practice/            ← 過去問・精進用
└── tools/
    ├── new.sh           ← コンテスト用ディレクトリを作る
    ├── add_sample.sh    ← サンプルを貼り付けで登録
    └── test.py          ← サンプルで AC/NG 判定
```

## コンテスト当日の流れ
```bash
cd ~/projects/AtCoder
tools/new.sh abc400              # a.py〜g.py と tests/ を作る
tools/add_sample.sh abc400 a     # 入力例・出力例を貼り付け（問題数ぶん繰り返す）
python3 tools/test.py abc400 a   # サンプルで確認 → 全部 AC なら a.py を提出
```
提出は a.py の中身をコピーして、言語「Python (CPython 3.13)」か「Python (PyPy 3.11)」で出す。ループが重い問題は PyPy の方が速い。

## 生成 AI のルール（必ず守る）
- ABC などのレーティング対象コンテストでは、コンテスト中に生成 AI へ問題文を渡したり、解法やコードを書かせたりすると違反になる
- 最新のルールは参加前に AtCoder の告知で確認する
- コンテストの前後に、AI で環境構築や解説の理解をするのは問題ない
