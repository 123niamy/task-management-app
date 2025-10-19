class Task:
    def __init__(self, id, title, description, due_date, priority, status="Incomplete"):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def __str__(self):
        return f"{self.id}: {self.title} [{self.status}]"
