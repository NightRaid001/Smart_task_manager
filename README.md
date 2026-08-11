# 🎯 Smart Task Manager

A command-line task manager with **AI-powered features** that helps users create, manage, and organize their tasks efficiently. Built with Python and integrated with Google Gemini AI for intelligent task breakdown.

## ✨ Features

- **📝 Add Tasks**: Create simple tasks with title and optional description
- **🤖 AI-Powered Subtask Generation**: Use Gemini AI to automatically break down complex tasks into 3-5 actionable subtasks
- **✅ Mark as Completed**: Track task completion status with visual indicators
- **📋 List All Tasks**: View all your tasks with their current status
- **🗑️ Delete Tasks**: Remove completed or unwanted tasks
- **💾 Data Persistence**: All tasks are stored in JSON format, preserving data across sessions
- **🧪 Unit Tests**: Comprehensive test suite for reliability and correctness

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Google Gemini API key (for AI features)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Smart_task_manager.git
cd Smart_task_manager
```

2. Create a virtual environment:
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your API key:
   - Create a `.env` file in the root directory
   - Add your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## 📖 Usage

Run the program:
```bash
python main.py
```

### Available Commands

1. **Agregar tarea** - Add a simple task with title and optional description
2. **Agregar tarea con IA** - Create a complex task and let AI generate subtasks automatically
3. **Completar tarea** - Mark a task as completed by its ID
4. **Listar tareas** - View all tasks with their status
5. **Eliminar tarea** - Delete a task by its ID
6. **Salir** - Exit the program

### Example Workflow

```
> 2 (AI-Powered Task Creation)
> Descripción: "Build a website with user authentication and payment system"
> The AI will generate 5 subtasks automatically
```

## 🏗️ Project Structure

```
Smart_task_manager/
├── main.py              # Entry point with CLI menu
├── task_manager.py      # Core TaskManager and Task classes
├── AI_service.py        # Google Gemini AI integration
├── test_task_manager.py # Unit tests
├── requirements.txt     # Project dependencies
├── tasks.json          # Persistent task storage
└── .env                # Environment variables (API keys)
```

## 🧪 Testing

Run the test suite:
```bash
python -m pytest test_task_manager.py
```

## 🤖 AI Integration

This project uses **Google Gemini AI** to intelligently break down complex tasks into manageable subtasks. The AI:
- Generates 3-5 clear and actionable subtasks
- Uses natural language processing to understand task descriptions
- Returns structured output in JSON format

## 📝 Technologies Used

- **Python 3.8+**
- **Google Gemini API** (AI models)
- **JSON** (Data persistence)
- **Python unittest/pytest** (Testing)

## 🗓️ Upcoming Features (Roadmap)

We're constantly working to improve the Smart Task Manager! Here are the features planned for future releases:

- **✏️ Edit Task Title & Description** - Modify existing task details without recreating them
- **⏰ Task Deadlines & Reminders** - Set due dates and receive notifications
- **🏷️ Task Categories & Tags** - Organize tasks with custom tags and categories for better filtering
- **🔍 Search & Filter Tasks** - Quickly find tasks by keyword, category, or status
- **📊 Task Statistics & Analytics** - View completion rates, productivity metrics, and trends
- **🔄 Recurring Tasks** - Create tasks that repeat on a schedule (daily, weekly, monthly)
- **💾 Export Tasks** - Export your tasks to CSV, PDF, or other formats
- **🌙 Dark Mode** - A sleek dark theme for comfortable viewing
- **🌐 Web Interface** - Web-based dashboard for managing tasks from any device
- **📱 Mobile App** - iOS and Android app for on-the-go task management
- **🔐 User Authentication** - Multi-user support with secure login
- **☁️ Cloud Sync** - Synchronize tasks across multiple devices

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or pull requests.

## 📄 License

See the LICENSE file for details.

---

**Thanks for checking out the Smart Task Manager!**

By NightRaid 🔥🤘
