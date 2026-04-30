from AI_service import create_subtasks
from task_manager import TaskManager

def print_menu():
        print("\n---- Gestor de tareas inteligente ----\n   ")
        print("Bienvenido al gestor de tareas inteligente. \n Aquí puedes agregar, completar, listar y eliminar tus tareas de manera eficiente. \n ¡Vamos a empezar! \n")
        print("Comandos disponibles:")
        print("1. Agregar tarea")
        print("2. Agregar tarea con IA (desglosar en subtareas)")
        print("3. Completar tarea")
        print("4. Listar tareas")
        print("5. Eliminar tarea")   
        print("6. Salir")

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
                description = input("Descripción de la tarea compleja: (no dejar el campo vacio): ").strip()
                if not description: # Validamos que la descripción no esté vacía antes de proceder
                    print("Error: La descripción no puede estar vacía.")
                    continue # Volver al menú principal si la descripción está vacía
                
                subtasks = create_subtasks(description) # Llamamos a la función para generar subtareas a partir de la descripción proporcionada por el usuario
                # Validamos si el primer elemento indica error y si subtasks es una lista antes de intentar agregar las subtareas al gestor
                for subtask in subtasks:
                    if not subtask.startswith("'Error"):
                        print(f"--- Creando {len(subtasks)} subtareas ---")
                        title = f"subtarea #{subtasks.index(subtask)+1}" # Creamos un título para cada subtarea utilizando la descripción generada por la función
                        manager.add_task(title, subtask) # Agregamos cada subtarea al gestor de tareas con un titulo y la descripción generada por la función
                        print("¡Tareas agregadas con éxito!")
                    else:
                        # Imprime el mensaje de error que viene de la función
                        print(subtasks[0] if subtasks else "Error: No se pudieron generar subtareas. Por favor, intenta con una descripción diferente.")
            case 3:
                task_id = int(input("ID de la tarea a completar: "))
                manager.complete_task(task_id) # Llamamos al método complete_task del gestor de tareas para marcar la tarea como completada utilizando el ID proporcionado por el usuario
            case 4:
                manager.list_tasks() # Llamamos al método list_tasks del gestor de tareas para mostrar todas las tareas actuales al usuario
            case 5:
                task_id = int(input("ID de la tarea a eliminar: "))
                manager.delete_task(task_id) # Llamamos al método delete_task del gestor de tareas para eliminar la tarea utilizando el ID proporcionado por el usuario
            case 6:
                print("¡Gracias por usar el gestor de tareas inteligente! ¡Hasta luego!")
                return
            case _:
                print("Comando no reconocido. Por favor, ingresa un comando válido.")

# El bloque if __name__ == "__main__": se utiliza para asegurarse de que el código dentro de este bloque solo se ejecute cuando el script se ejecute directamente, y no cuando se importe como un módulo en otro script. 
# En este caso, llama a la función main() para iniciar el programa.
if __name__ == "__main__":
    main()