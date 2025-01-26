from __future__ import annotations

from typing import TYPE_CHECKING
from multiprocessing import Process  

if TYPE_CHECKING:
    from lib.models.rules import Rule
    from lib.models.communicate import Communicator
    from argparse import Namespace

def producer(comunicator: Communicator, rules: list[Rule], args: Namespace):
    for rule in rules:
        comunicator.rules.put(rule)
    for _ in range(args.threads):
        comunicator.rules.put(None)

def Producer(comunicator: Communicator, rules: list[Rule], args: Namespace) -> Process:
    producer_ = Process(target=producer, args=(comunicator, rules, args))
    producer_.start()
    return producer_