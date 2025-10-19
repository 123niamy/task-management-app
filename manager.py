from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title, description, due_date, priority):
        task = Task(self.next_id, title, description, due_date, priority)
        self.tasks.append(task)
        self.next_id += 1

    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def mark_complete(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.status = "Complete"
                return True
        return False
