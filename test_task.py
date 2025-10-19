import unittest
from task import Task

class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task(1, "Test Task", "Description", "2025-10-20", "High")
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.status, "Incomplete")

    def test_task_str(self):
        task = Task(2, "Another Task", "Desc", "2025-10-21", "Low")
        self.assertEqual(str(task), "2: Another Task [Incomplete]")

if __name__ == "__main__":
    unittest.main()
