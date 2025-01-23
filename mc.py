import argparse
import os
import sys
from pathlib import Path
import multiprocessing
import time

from version import get_version
from lib.utils.rules import read_rules
from lib.workers import Producer, Scanner, Resulter

def get_args():
    parser = argparse.ArgumentParser(description="Malware Cleaner Tool")
    parser.add_argument(
        "-v", "--version", action="version", version=get_version()
    )
    parser.add_argument(
        "-c", "--config", action="store", dest="config", help="config file", type=Path, default=Path(os.getcwd()).joinpath("configs/")
    )
    parser.add_argument(
        "-d", "--debug", action="store_true", dest="debug", help="debug mode"
    )
    parser.add_argument(
        "-s", "--scan", action="store_true", dest="scan", help="scan mode"
    )
    parser.add_argument(
        "-r", "--remove", action="store_true", dest="remove", help="remove mode"
    )
    parser.add_argument(
        "-o", "--output", action="store", dest="output", help="output dir", type=Path, default=Path(os.getcwd()).joinpath("mc_out/")
    )
    parser.add_argument(
        "-t", "--threads", action="store", dest="threads", help="worker count, if 0 then maximum available", type=int, 
        default=0, choices=[0, *range(1, multiprocessing.cpu_count() + 1)]
    )
    parser.add_argument(
        "path", action="store", help="path to scan", type=Path
    )

    args = parser.parse_args(sys.argv[1:])

    if args.threads == 0:
        cpus = multiprocessing.cpu_count()
        if cpus <= 2:
            cpus = 1
        else:
            args.threads = cpus - 2

    return args

def main():
    args = get_args()
    # prepare rules
    rules = read_rules(args.config)
    # scan
    input_queue = multiprocessing.Queue()
    output_queue = multiprocessing.Queue()
    
    producer = multiprocessing.Process(target=Producer, args=(input_queue, rules, args.threads))
    producer.start()

    scanners: list[multiprocessing.Process] = []
    for _ in range(args.threads):
        scanner = multiprocessing.Process(target=Scanner, args=(args.path, input_queue, output_queue))
        scanner.start()
        scanners.append(scanner)

    resulter = multiprocessing.Process(target=Resulter, args=(output_queue, args.output, args.threads))
    resulter.start()

    producer.join()
    for scanner in scanners:
        scanner.join()
    resulter.join()

if __name__ == "__main__":
    start = time.time()
    main()
    print(f"Time: {time.time() - start}")