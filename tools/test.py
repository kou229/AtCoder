"""サンプルで動作確認する。

使い方: python3 tools/test.py abc400 a
contests/abc400/tests/a/*.in を a.py に入れ、*.out と比べる（行末の空白は無視）。
サンプルがなければ、標準入力から手入力して実行するだけ。
"""
import subprocess
import sys
import time
from pathlib import Path

root = Path(__file__).resolve().parent.parent
contest, prob = sys.argv[1], sys.argv[2]
src = root / "contests" / contest / f"{prob}.py"
cases = sorted((root / "contests" / contest / "tests" / prob).glob("*.in"))

if not cases:
    print("サンプルなし。入力を貼り付けて Ctrl-D:")
    subprocess.run([sys.executable, str(src)])
    sys.exit()


def norm(s):
    return [line.rstrip() for line in s.strip().splitlines()]


ok = 0
for case in cases:
    exp = case.with_suffix(".out").read_text()
    t = time.time()
    r = subprocess.run([sys.executable, str(src)], input=case.read_text(), capture_output=True, text=True, timeout=10)
    ms = (time.time() - t) * 1000
    if r.returncode == 0 and norm(r.stdout) == norm(exp):
        ok += 1
        print(f"AC  {case.stem}  {ms:.0f}ms")
    else:
        print(f"NG  {case.stem}  {ms:.0f}ms")
        print("--- 期待:\n" + exp.strip())
        print("--- 出力:\n" + r.stdout.strip())
        if r.stderr:
            print("--- エラー:\n" + r.stderr.strip())
print(f"{ok}/{len(cases)} AC")
