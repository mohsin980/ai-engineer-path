class User:
    def __init__(self, name, role):
        super().__init__(name, role)
        self.role = role

    def describe(self):
        return f"{self.name} is a {self.role}"