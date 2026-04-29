"""This module defines the Task and TaskManager classes for managing tasks in a simple task management application. The Task class represents an individual task with attributes such as id, title, description, and completion status. The TaskManager class provides methods to add, retrieve, complete, list, and delete tasks. This separation of concerns allows for better organization and maintainability of the code. The TaskManager class maintains a list of tasks and handles the logic for managing them, while the Task class serves as a data structure for representing individual tasks.
"""

import json


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

    FILENAME = "tasks.json"

    def __init__(self) -> None:
        """Inicializa el TaskManager con una lista vacía de tareas y un contador de ID para asignar a las nuevas tareas.
        Arguments:
            None
        Returns:
            None
        """
        self._tasks = []
        self.next_id = 1
        self.load_tasks()

    def add_task(self, title: str, description: str = "") -> Task:
        """Agrega una nueva tarea al TaskManager con un título y una descripción opcional.  La tarea se asigna automáticamente un ID único.
        Arguments:
            title: El título de la tarea.
            description: Una descripción opcional de la tarea.
        Returns:
            La tarea recién creada.
        """
        task = Task(id=self.next_id, title=title, description=description)
        self._tasks.append(task)
        self.next_id += 1
        print(f" \n Tarea agregada: {task} con el ID: {task.id}")
        self.save_tasks()
        return task

    def get_task(self, task_id: int) -> Task:
        """Obtiene una tarea por su ID.
        Arguments: 
            task_id: El ID de la tarea a obtener.
        Returns:
            La tarea con el ID especificado.
        Raises:
            ValueError: Si no se encuentra una tarea con el ID especificado.
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        raise ValueError(f"\n Tarea con ID {task_id} no encontrada.")

    def complete_task(self, task_id: int) -> None:
        """Marca una tarea como completada.
        Arguments:
            task_id: El ID de la tarea a completar.
        Returns:
            None
        Raises:
            ValueError: Si no se encuentra una tarea con el ID especificado.
        """
        if not self._tasks:
            print(" \n La tarea con ese ID no existe. Por favor, ingresa un ID válido.")
            return
        else:
            task = self.get_task(task_id)
            task.completed = True
            self.save_tasks()
            print(f" \n Tarea completada: {task} con el ID: {task.id}")

    def list_tasks(self) -> None:
        """Lista todas las tareas en el TaskManager.    
        Arguments:
            None
        Returns:
            None
        """
        if not self._tasks:
            print(" \n  No hay tareas para mostrar.")
        else:
            for task in self._tasks:
                print(task)
    
    def delete_task(self, task_id: int) -> None:
        """Elimina una tarea por su ID.
        Arguments:
            task_id: El ID de la tarea a eliminar.
        Returns:
            None
        Raises:
            ValueError: Si no se encuentra una tarea con el ID especificado.
        """
        task = self.get_task(task_id)
        self._tasks.remove(task)
        self.save_tasks()
        print(f" \n Tarea eliminada: {task} con el ID: {task.id}")



    #functions for saving and loading tasks from a file

    def load_tasks(self) -> None:
        """Carga las tareas desde un archivo JSON.
        Arguments:
            None
        Returns:
            None
        Raises:
            FileNotFoundError: Si el archivo de tareas no existe.
        """
        try:
            with open(self.FILENAME, "r") as file:
                tasks_data = json.load(file)
                self._tasks = [Task(item["id"], item["title"], item["description"], item["completed"]) for item in tasks_data]
                if self._tasks:
                    self._next_id = self._tasks[-1].id + 1
                else:
                    self._next_id = 1
            
        except FileNotFoundError:
            self._tasks = []
        
    def save_tasks(self) -> None:
        """Guarda las tareas en un archivo JSON.
        Arguments:
            None
        Returns:
            None
        """
        with open(self.FILENAME, "w") as file:
            json.dump([{"id": task.id, "title": task.title, "description": task.description, "completed": task.completed} for task in self._tasks], file, indent=4)
