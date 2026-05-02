from services.task_service import TaskService

service = TaskService()

service.add_task("Homework", "School")
service.add_task("Workout", "Personal")

service.mark_completed("Homework")

for task in service.get_all_tasks():
    print(task)
