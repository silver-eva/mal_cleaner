from __future__ import annotations
from typing import TYPE_CHECKING

import time
from multiprocessing import Process

if TYPE_CHECKING:
    from pathlib import Path

    from lib.models.rules import Rule
    from lib.models.communicate import Communicator

def scanner(scan_dir: Path, communicator: Communicator):
    while True:
        rule: Rule = communicator.rules.get()
        if rule is None:
            break
        print(rule)
        time.sleep(1)
        communicator.output.put(f"Processed by {rule.name} in {scan_dir}")
    communicator.output.put(None)

def Scanner(scan_dir: Path, communicator: Communicator) -> Process:
    scanner_ = Process(target=scanner, args=(scan_dir, communicator))
    scanner_.start()
    return scanner_