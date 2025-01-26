
from enum import Enum
from pathlib import Path

class Actions(Enum):
    delete = "delete"
    locate = "locate"


    def _locate(self, file: Path) -> str:
        return f"[+] Located: {file.resolve()}"

    def _delete(self, file: Path) -> str:
        file.unlink()
        return f"[X] Deleted: {file.resolve()}"

    def run(self, file: Path):
        if self == Actions.delete:
            return self._delete(file)
        elif self == Actions.locate:
            return self._locate(file)

class Types(Enum):
    file = "file"
    directory = "directory"
    registry = "registry"