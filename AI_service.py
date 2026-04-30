"""
This file is used to set environment variables for the project. It is typically used to store sensitive information such as API keys, database credentials, and other configuration settings that should not be hardcoded in the source code. 
The variables defined in this file can be accessed by the application at runtime, allowing for greater flexibility and security.
The .env file is usually included in the .gitignore file to prevent it from being committed to version control, ensuring that sensitive information is not exposed in public repositories.
"""
#import google.generativeai as genai #libreria obsoleta, se debe usar google.genai
import os
import json
from dotenv import load_dotenv # Librería para cargar variables de entorno desde un archivo .env
from google import genai # Importamos el módulo genai del paquete google para interactuar con los servicios de inteligencia artificial de Google, como Gemini. Este módulo proporciona las herramientas necesarias para enviar solicitudes y recibir respuestas del modelo de lenguaje de Google.
from google.genai import types # Importamos el módulo types del paquete google.genai para acceder a las clases y tipos de datos específicos que se utilizan al interactuar con los servicios de inteligencia artificial de Google, como Gemini. Este módulo incluye definiciones para configurar las solicitudes y manejar las respuestas del modelo de lenguaje de Google.

# Cargar las variables de entorno desde el archivo .env
load_dotenv()
# Configurar la clave de API para el cliente de Gemini utilizando la variable de entorno GEMINI_API_KEY
api_key=os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def create_subtasks(description):
    """
    Esta función toma una descripción de una tarea compleja como entrada y utiliza el modelo de lenguaje de Google Gemini para generar una lista de subtareas claras y concisas que desglosan la tarea principal en pasos más manejables.
    La función primero verifica si la clave de API está configurada, luego construye un prompt detallado para solicitar al modelo que genere subtareas específicas, y finalmente procesa la respuesta para extraer las subtareas en una lista. 
    Si ocurre algún error durante el proceso, la función devuelve un mensaje de error descriptivo.
    Arguments:
    description (str): Una descripción detallada de la tarea compleja que se desea desglosar en subtareas.
    Returns:
    list: Una lista de subtareas generadas por el modelo de lenguaje de Google Gemini, o un mensaje de error si no se pudieron generar las subtareas.
    """
    
    if not api_key: # Verificar si la clave de API está configurada antes de intentar usarla. Si no está configurada, se devuelve un mensaje de error.
        return ["Error: La clave de API no está configurada.Por favor, establece la variable de entorno GEMINI_API_KEY con tu clave de API de Gemini"]
    try:
        # Crear el prompt para desglosar la tarea en subtareas claras y concisas, utilizando la descripción proporcionada por el usuario. 
        # El prompt incluye instrucciones claras sobre cómo formatear
        # la respuesta, indicando que cada subtarea debe comenzar con un guion (-) para facilitar su identificación y extracción posterior.
        
        prompt = f"""
        Desglosa la tarea en 3 a 5 subtareas claras y concisas para realizarlas.
        Tarea: {description}
        Responde con una lista de subtareas, cada una en una línea separada, comenzando con un guion (-).
        Ejemplo:
        - Subtarea 1: Descripción breve y accionable de la primera subtarea.
        - Subtarea 2: Descripción breve y accionable de la segunda subtarea.
        - Subtarea 3: Descripción breve y accionable de la tercera subtarea
        - Subtarea 4: Descripción breve y accionable de la cuarta subtarea
        - Subtarea 5: Descripción breve y accionable de la quinta subtarea

        la descripción de cada subtarea debe ser breve y accionable, evitando ambigüedades. 
        Cada subtarea debe comenzar con un guion (-) para facilitar su identificación y extracción posterior.
        """

        # Enviar el prompt al modelo de lenguaje Gemini para generar las subtareas, utilizando la configuración especificada para controlar la creatividad y la diversidad de la respuesta.
        response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=types.Part.from_text(text=prompt),
        config=types.GenerateContentConfig(
            temperature=0.1,
            top_p=0.95,
            top_k=20,
            response_mime_type="application/json"
        ),
        )

        if response.text: # Se verifica si la respuesta contiene texto antes de intentar imprimirlo.
            content = response.text.strip()
            subtasks = []
            try:
                # Parsear el JSON array que devuelve Gemini
                tasks_list = json.loads(content)
                # Iterar sobre cada elemento del array
                for task in tasks_list:
                    task = task.strip()
                    # Eliminar el guion inicial si existe
                    if task.startswith("-"):
                        task = task[1:].strip()
                    if task:
                        subtasks.append(task)
                        
            except json.JSONDecodeError:
                # Si no es JSON válido, intentar parseo por líneas (fallback)
                for line in content.split("\n"):
                    line = line.strip()
                    if line and line.startswith("-"):
                        subtask = line[1:].strip()
                        if subtask:
                            subtasks.append(subtask)

            return subtasks if subtasks else "Error: No se pudieron generar subtareas. Por favor, intenta con una descripción diferente."
        else:
            return "Error: No se recibió una respuesta de texto del modelo. Por favor, intenta nuevamente."

    except Exception as e:
        return f"Error: {str(e)}"


