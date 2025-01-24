

class Rule:
    def __init__(self, rule: dict):
        self.name = rule.get("name")
        self.description = rule.get("description")
        self.author = rule.get("author")
        self.pattern = rule.get("pattern")
        self.action = rule.get("action")

    def __str__(self):
        output = " ".join([f"{key}: {value}" for key, value in self.__dict__.items()])
        return output
