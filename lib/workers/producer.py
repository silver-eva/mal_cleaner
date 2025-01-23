from __future__ import annotations

from typing import TYPE_CHECKING    

if TYPE_CHECKING:
    from multiprocessing import Queue
    from lib.models.rules import Rule

def producer(rules_q: Queue, rules: list[Rule], workers_count: int):
    for rule in rules:
        rules_q.put(rule)
    for _ in range(workers_count):
        rules_q.put(None)