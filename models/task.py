class Task:
    def __init__(self, title, category):
        self.title = title
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        return f"{self.title} | {self.category} | {'Done' if self.completed else 'Pending'}"
