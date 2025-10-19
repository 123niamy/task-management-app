import unittest
from manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        self.manager.add_task("Test", "Desc", "2025-10-20", "Medium")
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0].title, "Test")

    def test_mark_complete(self):
        self.manager.add_task("Test", "Desc", "2025-10-20", "Medium")
        result = self.manager.mark_complete(1)
        self.assertTrue(result)
        self.assertEqual(self.manager.tasks[0].status, "Complete")

if __name__ == "__main__":
    unittest.main()
