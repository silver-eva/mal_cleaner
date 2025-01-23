

class Rule:
    def __init__(self, name: str, pattern: str, action: str):
        self.name = name
        self.pattern = pattern
        self.action = action

    def __str__(self):
        return f"{self.name} {self.pattern} {self.action}"
