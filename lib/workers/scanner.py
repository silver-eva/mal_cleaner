from __future__ import annotations
from typing import TYPE_CHECKING

import time

if TYPE_CHECKING:
    from pathlib import Path

    from multiprocessing import Queue
    from lib.models.rules import Rule

def scanner(scan_dir: Path, rules_q: Queue, output_q: Queue):
    while True:
        rule: Rule = rules_q.get()
        if rule is None:
            break
        print(rule)
        time.sleep(1)
        output_q.put(f"Processed by {rule.name} in {scan_dir}")
    output_q.put(None)