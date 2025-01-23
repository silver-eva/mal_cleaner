from typing import Literal
from pathlib import Path

from lib.utils.readers import Reader, readers_map
from lib.models.rules import Rule

def read_config(path:Path, reader: Reader) -> list[Rule]:
    return reader.read(path)

def read_config_dir(path:Path, reader: Reader) -> dict:
    rules = []
    for file in path.iterdir():
        if file.suffix == reader:
            rules.extend(read_config(file, reader))
    return rules

def read_rules(path:Path, format: Literal["yaml"] = "yaml") -> list:
    reader = readers_map[format]
    if path.is_file():
        rules = read_config(path, reader)
    elif path.is_dir():
        rules = read_config_dir(path, reader)
    return rules

