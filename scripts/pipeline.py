# -*- coding: utf-8 -*-
"""顺序执行 crawl -> check -> build。"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

for stage in ("crawl.py", "check.py", "build.py"):
    print(f"=== {stage} ===")
    r = subprocess.run([sys.executable, os.path.join(HERE, stage)])
    if r.returncode != 0:
        sys.stderr.write(f"[pipeline] {stage} 失败，退出码 {r.returncode}\n")
        sys.exit(r.returncode)
print("[pipeline] done")
