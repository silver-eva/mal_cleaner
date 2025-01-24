from __future__ import annotations
from typing import TYPE_CHECKING

from multiprocessing import Process

if TYPE_CHECKING:
    from pathlib import Path
    from lib.models.communicate import Communicator


def resulter(communicator: Communicator, output_dir: Path, workers_count: int):
    
    report_file = output_dir.joinpath("report.txt")
    report_file.touch(exist_ok=True)

    with open(report_file, "w") as f:
        end_signals_received = 0
        while end_signals_received < workers_count:
            result: str = communicator.output.get()
            if result is None:
                end_signals_received += 1
            else:
                f.write(f"{result}\n")

def Resulter(comunicator: Communicator, output_dir: Path, workers_count: int) -> Process:
    resulter_ = Process(target=resulter, args=(comunicator, output_dir, workers_count))
    resulter_.start()
    return resulter_
