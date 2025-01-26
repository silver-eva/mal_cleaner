from pathlib import Path
from lib.models.literals import Actions, Types

class Rule:
    def __init__(self, rule: dict):
        self.name = rule.get("name")
        self.description = rule.get("description")
        self.author = rule.get("author")
        self.pattern = rule.get("pattern")
        self.type =  Types(rule.get("type"))
        self.action = Actions(rule.get("action"))

    def __str__(self):
        output = " ".join([f"{key}: {value}" for key, value in self.__dict__.items()])
        return output
    
    def _locate_files(self, target_dir: Path):
        located_files = list(target_dir.rglob(self.pattern, case_sensitive=False))
        return located_files
    
    def exec(self, target_dir: Path, mode: str):
        located_files = self._locate_files(target_dir)

        rule_report_part = f"{self.name} - {self.description} - {self.author}"

        for file in located_files:
            if mode == "locate":
                print(self.action._locate(file),"|", rule_report_part)
            elif mode == "rule":
                print(self.action.run(file),"|", rule_report_part)
                
                



