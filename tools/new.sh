#!/bin/bash
# 使い方: tools/new.sh abc400        → contests/abc400/{a..g}.py を作る
#         tools/new.sh abc400 a b c  → 指定した問題だけ作る
set -eu
cd "$(dirname "$0")/.."
contest=$1; shift
problems=${@:-a b c d e f g}
dir=contests/$contest
mkdir -p "$dir"
for p in $problems; do
  [ -e "$dir/$p.py" ] || cp python/template.py "$dir/$p.py"
  mkdir -p "$dir/tests/$p"
  if command -v oj >/dev/null && [ -z "$(ls "$dir/tests/$p")" ]; then
    oj download -d "$dir/tests/$p" "https://atcoder.jp/contests/$contest/tasks/${contest}_$p" >/dev/null 2>&1 \
      && echo "$p: サンプル取得" || echo "$p: サンプル取得失敗（tools/add_sample.sh で手で追加）"
  fi
done
echo "作成: $dir"
