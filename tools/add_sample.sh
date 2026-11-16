#!/bin/bash
# 使い方: tools/add_sample.sh abc400 a
# 問題ページの「入力例」「出力例」を順に貼り付けて登録する（それぞれ Ctrl-D で確定）
set -eu
cd "$(dirname "$0")/.."
dir=contests/$1/tests/$2
mkdir -p "$dir"
n=$(( $(ls "$dir"/*.in 2>/dev/null | wc -l) + 1 ))
echo "入力例 $n を貼り付けて Ctrl-D:"; cat > "$dir/sample-$n.in"
echo "出力例 $n を貼り付けて Ctrl-D:"; cat > "$dir/sample-$n.out"
echo "登録: $dir/sample-$n"
