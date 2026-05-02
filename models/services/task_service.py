from models.task import Task

class TaskService:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, category):
        task = Task(title, category)
        self.tasks.append(task)

    def delete_task(self, title):
        self.tasks = [t for t in self.tasks if t.title != title]

    def mark_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()

    def get_all_tasks(self):
        return self.tasks


def edit_task(self, old_title, new_title, new_category):
    for task in self.tasks:
        if task.title == old_title:
            task.title = new_title
            task.category = new_category
