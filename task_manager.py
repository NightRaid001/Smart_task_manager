class Task:
    def __init__(self, id: int, title: str, description: str = "", completed: bool = False) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def __str__(self) -> str:
        status = "✅" if self.completed else "Pending"
        return f"Task ID: [{status}] #{self.id}: {self.title}, Description: {self.description}"
    
class TaskManager:

    def __init__(self) -> None:
        self.tasks = []
        self.next_id = 1

    def add_task(self, title: str, description: str = "") -> Task:
        task = Task(id=self.next_id, title=title, description=description)
        self.tasks.append(task)
        self.next_id += 1
        print(f"Added task: {task}")
        return task

    def get_task(self, task_id: int) -> Task:
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise ValueError(f"Task with ID {task_id} not found.")

    def complete_task(self, task_id: int) -> None:
        task = self.get_task(task_id)
        task.completed = True
        print(f"Completed task: {task}")

    def list_tasks(self) -> list[Task]:
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)
    
    def delete_task(self, task_id: int) -> None:
        task = self.get_task(task_id)
        self.tasks.remove(task)
        print(f"Deleted task: {task}")