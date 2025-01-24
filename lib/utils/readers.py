import yaml
from pathlib import Path

from lib.models.rules import Rule


class Reader:
    suffix = None

    @staticmethod
    def read(self, path:Path) -> list[Rule]:
        raise NotImplementedError
    
    def __eq__(self, value):
        return value == self.suffix
    
class YamlReader(Reader):
    suffix = [".yaml", ".yml"]

    @staticmethod
    def read(path:Path) -> list[Rule]:
        with open(path) as f:
            rules: dict = yaml.safe_load(f)
        return [Rule(rule) for rule in rules]
    
    def __eq__(self, value):
        return value in self.suffix

   
readers_map = {
    "yaml": YamlReader()
}