from __future__ import annotations

from typing import TYPE_CHECKING
from multiprocessing import Process  

if TYPE_CHECKING:
    from lib.models.rules import Rule
    from lib.models.communicate import Communicator

def producer(comunicator: Communicator, rules: list[Rule], workers_count: int):
    for rule in rules:
        comunicator.rules.put(rule)
    for _ in range(workers_count):
        comunicator.rules.put(None)

def Producer(comunicator: Communicator, rules: list[Rule], workers_count: int) -> Process:
    producer_ = Process(target=producer, args=(comunicator, rules, workers_count))
    producer_.start()
    return producer_