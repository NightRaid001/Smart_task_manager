"""This module contains unit tests for the TaskManager class defined in task_manager.py. 
The tests cover the main functionalities of the TaskManager, including adding tasks, deleting tasks, listing tasks, and completing tasks. 
The tests use the unittest framework and mock file I/O operations to avoid actual file interactions during testing. 
Each test checks for the expected behavior of the TaskManager methods and ensures that the appropriate print statements are called with the correct output. 
This helps to verify that the TaskManager class is functioning as intended and can handle various scenarios, including edge cases such as attempting to delete a non-existent task.
"""

import unittest
from unittest.mock import patch, mock_open
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self) -> None:
        """Set up a TaskManager instance for testing, while mocking the load_tasks and save_tasks methods to avoid file I/O."""
        with patch.object(TaskManager, 'load_tasks'), patch.object(TaskManager, 'save_tasks'):
            self.tm = TaskManager()

    @patch("builtins.open", new_callable=mock_open)
    def test_add_task(self, mock_file)-> None:
        """Test the add_task method of TaskManager. It checks if a task is added correctly and if the appropriate print statement is called."""
        with patch("builtins.print") as mock_print:
            self.tm.add_task("Test Task")
            # The print includes the task details and ID
            expected_call = f" \n Tarea agregada: \n\n Estado de la tarea: Pendiente \n ID: 1 \n titulo: Test Task \n Descripción:  con el ID: 1"
            mock_print.assert_called_with(expected_call)
        self.assertEqual(len(self.tm._tasks), 1)
        self.assertEqual(self.tm._tasks[0].title, "Test Task")

    @patch("builtins.open", new_callable=mock_open)
    def test_delete_task(self, mock_file)-> None:
        """Test the delete_task method of TaskManager. It checks if a task is deleted correctly and if the appropriate print statement is called."""
        self.tm.add_task("Task to delete")
        task_id = self.tm._tasks[0].id
        with patch("builtins.print") as mock_print:
            self.tm.delete_task(task_id)
            expected_call = f" \n Tarea eliminada: \n\n Estado de la tarea: Pendiente \n ID: {task_id} \n titulo: Task to delete \n Descripción:  con el ID: {task_id}"
            mock_print.assert_called_with(expected_call)
        self.assertEqual(len(self.tm._tasks), 0)

    @patch("builtins.open", new_callable=mock_open)
    def test_delete_nonexistent_task(self, mock_file)-> None:
        """Test the delete_task method with a non-existent task ID."""
        with self.assertRaises(ValueError) as context:
            self.tm.delete_task(999)
        self.assertIn("Tarea con ID 999 no encontrada", str(context.exception))

    @patch("builtins.open", new_callable=mock_open)
    def test_list_tasks(self, mock_file)-> None:
        """Test the list_tasks method of TaskManager."""
        self.tm.add_task("Task 1")
        self.tm.add_task("Task 2")
        with patch("builtins.print") as mock_print:
            self.tm.list_tasks()
            self.assertTrue(mock_print.call_count >= 2)

    @patch("builtins.open", new_callable=mock_open)
    def test_complete_task(self, mock_file)-> None:
        """Test the complete_task method of TaskManager."""
        self.tm.add_task("Task to complete")
        task_id = self.tm._tasks[0].id
        with patch("builtins.print") as mock_print:
            self.tm.complete_task(task_id)
            expected_call = f" \n Tarea completada: \n\n Estado de la tarea: ✅ \n ID: {task_id} \n titulo: Task to complete \n Descripción:  con el ID: {task_id}"
            mock_print.assert_called_with(expected_call)
        self.assertTrue(self.tm._tasks[0].completed)

if __name__ == "__main__":
    unittest.main()
