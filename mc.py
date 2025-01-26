from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from multiprocessing import Process

import argparse
import os
import sys
import time
from multiprocessing import cpu_count
from pathlib import Path

from version import get_version
from lib.utils.rules import read_rules
from lib.workers import Producer, Scanner, Resulter
from lib.models.communicate import Communicator

def get_args():
    cpus = cpu_count()

    parser = argparse.ArgumentParser(description="Malware Cleaner Tool")
    parser.add_argument(
        "-v", "--version", action="version", version=get_version()
    )
    parser.add_argument(
        "-c", "--config", action="store", dest="config", help="rules path", type=Path, default=Path(os.getcwd()).joinpath("rules/")
    )
    parser.add_argument(
        "-d", "--debug", action="store_true", dest="debug", help="debug mode"
    )
    parser.add_argument(
        "-l", "--locate", action="store_true", dest="locate", help="locate mode"
    )
    parser.add_argument(
        "-o", "--output", action="store", dest="output", help="output dir", type=Path, default=Path(os.getcwd()).joinpath("reports/")
    )
    parser.add_argument(
        "-t", "--threads", action="store", dest="threads", help="worker count, if 0 then maximum available", type=int, 
        default=0, choices=[0, *range(1, cpus + 1)]
    )
    parser.add_argument(
        "path", action="store", help="path to scan", type=Path
    )

    args = parser.parse_args(sys.argv[1:])

    if args.threads == 0:
        if cpus <= 2:
            cpus = 1
        else:
            args.threads = cpus - 2
    
    if not args.config.exists():
        parser.error(f'Rules path [{args.input_dir}] is not exist')
    
    if args.output.exists() and any(args.output.iterdir()):
        user_input = input(f"Output directory [{args.output}] is not empty. Continue? [y/n]: ")
        if user_input.lower() != "y":
            sys.exit(0)
    elif not args.output.exists():
        args.output.mkdir(parents=True)

    if args.locate:
        args.mode = "locate"
    else:
        args.mode = "rule"

    return args

def main():
    args = get_args()
    # prepare rules
    rules = read_rules(args.config)
    comunicator = Communicator()

    # setup workers pool
    workers: list[Process] = []
    workers.append(Producer(comunicator, rules, args))
    for _ in range(args.threads):
        workers.append(Scanner(args, comunicator))
    workers.append(Resulter(comunicator, args))

    start = time.time()

    for worker in workers:
        worker.join()
    
    print(f"Time: {time.time() - start}")

if __name__ == "__main__":
    main()
    