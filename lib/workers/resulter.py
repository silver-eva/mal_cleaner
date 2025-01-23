from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from multiprocessing import Queue
    from pathlib import Path


def resulter(output_q: Queue, output_dir: Path, workers_count: int):
    
    report_file = output_dir.joinpath("report.txt")
    report_file.touch(exist_ok=True)

    with open(report_file, "w") as f:
        end_signals_received = 0
        while end_signals_received < workers_count:
            result: str = output_q.get()
            if result is None:
                end_signals_received += 1
            else:
                f.write(f"{result}\n")
