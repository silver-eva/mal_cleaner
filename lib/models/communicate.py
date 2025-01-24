from dataclasses import dataclass
from multiprocessing import Queue

@dataclass
class Communicator:
    rules: Queue = Queue()
    output: Queue = Queue()
