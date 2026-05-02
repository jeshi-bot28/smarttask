from services.task_service import TaskService
from storage.json_storage import JSONStorage

def test_add_task():
    storage = JSONStorage()
    service = TaskService(storage)

    service.add_task("Test Task", "School")

    assert len(service.get_all_tasks()) > 0


def test_mark_completed():
    storage = JSONStorage()
    service = TaskService(storage)

    service.add_task("Test Task", "School")
    service.mark_completed("Test Task")

    task = service.get_all_tasks()[0]
    assert task.completed == True


def test_delete_task():
    storage = JSONStorage()
    service = TaskService(storage)

    service.add_task("Delete Me", "Work")
    service.delete_task("Delete Me")

    assert len(service.get_all_tasks()) == 0
