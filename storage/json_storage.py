import json
from models.task import Task

class JSONStorage:

    def save(self, tasks):
        data = []
        for t in tasks:
            data.append({
                "title": t.title,
                "category": t.category,
                "completed": t.completed
            })

        with open("tasks.json", "w") as f:
            json.dump(data, f)

    def load(self):
        tasks = []
        try:
            with open("tasks.json", "r") as f:
                data = json.load(f)
                for item in data:
                    task = Task(item["title"], item["category"])
                    task.completed = item["completed"]
                    tasks.append(task)
        except FileNotFoundError:
            pass

        return tasks
