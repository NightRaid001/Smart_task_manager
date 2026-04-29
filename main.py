from task_manager import TaskManager
def print_menu():
        print("\n---- Gestor de tareas inteligente ----\n   ")
        print("Bienvenido al gestor de tareas inteligente. \n Aquí puedes agregar, completar, listar y eliminar tus tareas de manera eficiente. \n ¡Vamos a empezar! \n")
        print("Comandos disponibles:")
        print("1. Agregar tarea")
        print("2. Completar tarea")
        print("3. Listar tareas")
        print("4. Eliminar tarea")   
        print("5. Salir")

def main():

    manager = TaskManager()

    while True:

        print_menu()
        choice = int(input("\n Ingresa un comando: ").strip())
        match choice:
            case 1:
                title = input("ingresa el título de la tarea: ")
                description = input("Descripción de la tarea (opcional): ")
                manager.add_task(title, description)
            case 2:
                task_id = int(input("ID de la tarea a completar: "))
                manager.complete_task(task_id)
            case 3:
                manager.list_tasks()
            case 4:
                task_id = int(input("ID de la tarea a eliminar: "))
                manager.delete_task(task_id)
            case 5:
                print("¡Gracias por usar el gestor de tareas inteligente! ¡Hasta luego!")
                return
            case _:
                print("Comando no reconocido. Por favor, ingresa un comando válido.")

if __name__ == "__main__":
    main()