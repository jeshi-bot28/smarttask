from services.task_service import TaskService

service = TaskService()

# Add tasks
service.add_task("Homework", "School")
service.add_task("Workout", "Personal")
service.add_task("Project", "Work")

# Edit task
service.edit_task("Project", "Final Project", "School")

# Mark complete
service.mark_completed("Homework")

# Show all tasks
print("ALL TASKS:")
for task in service.get_all_tasks():
    print(task)

# Filter by category
print("\nSCHOOL TASKS:")
for task in service.filter_by_category("School"):
    print(task)

# Filter by completed
print("\nCOMPLETED TASKS:")
for task in service.filter_by_status(True):
    print(task)
