class Task:
    def __init__(self, title, category):
        self.title = title
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True


tasks = []

tasks.append(Task("Homework", "School"))
tasks.append(Task("Workout", "Personal"))

tasks[0].mark_completed()

for t in tasks:
    print(t.title, t.category, t.completed)
