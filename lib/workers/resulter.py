from __future__ import annotations
from typing import TYPE_CHECKING

from multiprocessing import Process

if TYPE_CHECKING:
    from pathlib import Path
    from lib.models.communicate import Communicator
    from argparse import Namespace


def resulter(communicator: Communicator, args: Namespace):
    
    report_file = args.output.joinpath("report.txt")
    report_file.touch(exist_ok=True)

    with open(report_file, "w") as f:
        end_signals_received = 0
        while end_signals_received < args.threads:
            result: str = communicator.output.get()
            if result is None:
                end_signals_received += 1
            else:
                f.write(f"{result}\n")

def Resulter(comunicator: Communicator, args: Namespace) -> Process:
    resulter_ = Process(target=resulter, args=(comunicator, args))
    resulter_.start()
    return resulter_
