"""This module defines the Task and TaskManager classes for managing tasks in a simple task management application. The Task class represents an individual task with attributes such as id, title, description, and completion status. The TaskManager class provides methods to add, retrieve, complete, list, and delete tasks. This separation of concerns allows for better organization and maintainability of the code. The TaskManager class maintains a list of tasks and handles the logic for managing them, while the Task class serves as a data structure for representing individual tasks.
"""

class Task:
    def __init__(self, id: int, title: str, description: str = "", completed: bool = False) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def __str__(self) -> str:
        status = "✅" if self.completed else "Pendiente"
        return f"\n\n Estado de la tarea: {status} \n ID: {self.id} \n titulo: {self.title} \n Descripción: {self.description}"
    
class TaskManager:

    def __init__(self) -> None:
        self.tasks = []
        self.next_id = 1

    def add_task(self, title: str, description: str = "") -> Task:
        task = Task(id=self.next_id, title=title, description=description)
        self.tasks.append(task)
        self.next_id += 1
        print(f" \n Tarea agregada: {task} con el ID: {task.id}")
        return task

    def get_task(self, task_id: int) -> Task:
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise ValueError(f"\n Tarea con ID {task_id} no encontrada.")

    def complete_task(self, task_id: int) -> None:
        if not self.tasks:
            print(" \n La tarea con ese ID no existe. Por favor, ingresa un ID válido.")
            return
        else:
            task = self.get_task(task_id)
            task.completed = True
            print(f" \n Tarea completada: {task} con el ID: {task.id}")

    def list_tasks(self) -> None:
        if not self.tasks:
            print(" \n  No hay tareas para mostrar.")
        else:
            for task in self.tasks:
                print(task)
    
    def delete_task(self, task_id: int) -> None:
        task = self.get_task(task_id)
        self.tasks.remove(task)
        print(f" \n Tarea eliminada: {task} con el ID: {task.id}")