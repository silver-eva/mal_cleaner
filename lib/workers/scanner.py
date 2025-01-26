from __future__ import annotations
from typing import TYPE_CHECKING

import time
from multiprocessing import Process
import os

if TYPE_CHECKING:
    from lib.models.rules import Rule
    from lib.models.communicate import Communicator
    from argparse import Namespace

def scanner(args: Namespace, communicator: Communicator):
    root_path = args.path
    while True:
        rule: Rule = communicator.rules.get()
        if rule is None:
            break
        try:
            rule.exec(root_path, args.mode)
        except Exception as e:
            print(rule, e.__class__.__name__, e)
        time.sleep(1)
        communicator.output.put(f"Worker: {os.getpid()}:",f"{rule.name} - {rule.description} - {rule.author}")
    communicator.output.put(None)

def Scanner(args: Namespace, communicator: Communicator) -> Process:
    scanner_ = Process(target=scanner, args=(args, communicator))
    scanner_.start()
    return scanner_