Python
                         Копировать
                    """
                    Архитектура MVC (Model-View-Controller) для Todo приложения
                    Model - бизнес-логика и данные
                    View - отображение данных
                    Controller - обработка пользовательского ввода
                    """

                    from abc import ABC, abstractmethod
                    from datetime import datetime
                    from typing import List, Optional

                    # ==================== MODEL (МОДЕЛЬ) ====================

                    class Task:
                    """Модель задачи"""

                    def __init__(self, id: int, title: str, description: str = "",
                    completed: bool = False, priority: int = 2):
                    self.id = id
                    self.title = title
                    self.description = description
                    self.completed = completed
                    self.priority = priority  # 1-высокий, 2-средний, 3-низкий
                    self.created_at = datetime.now()
                    self.updated_at = datetime.now()

                    def toggle_complete(self):
                    """Переключение статуса выполнения"""
                    self.completed = not self.completed
                    self.updated_at = datetime.now()

                    def update(self, title: str = None, description: str = None, priority: int = None):
                    """Обновление задачи"""
                    if title is not None:
                    self.title = title
                    if description is not None:
                    self.description = description
                    if priority is not None:
                    self.priority = priority
                    self.updated_at = datetime.now()

                    def __str__(self):
                    status = "✓" if self.completed else "✗"
                    priority_map = {1: "🔴", 2: "🟡", 3: "🟢"}
                    return f"{status} [{self.id}] {self.title} {priority_map.get(self.priority, '')}"


                    class TaskModel:
                    """Модель для управления задачами"""

                    def __init__(self):
                    self.tasks: List[Task] = []
                    self.next_id = 1

                    def add_task(self, title: str, description: str = "", priority: int = 2) -> Task:
                    """Добавление новой задачи"""
                    task = Task(self.next_id, title, description, False, priority)
                    self.tasks.append(task)
                    self.next_id += 1
                    return task

                    def get_task(self, task_id: int) -> Optional[Task]:
                    """Получение задачи по ID"""
                    for task in self.tasks:
                    if task.id == task_id:
                    return task
                    return None

                    def get_all_tasks(self) -> List[Task]:
                    """Получение всех задач"""
                    return self.tasks

                    def get_tasks_by_status(self, completed: bool) -> List[Task]:
                    """Получение задач по статусу выполнения"""
                    return [task for task in self.tasks if task.completed == completed]

                    def update_task(self, task_id: int, **kwargs) -> Optional[Task]:
                    """Обновление задачи"""
                    task = self.get_task(task_id)
                    if task:
                    task.update(**kwargs)
                    return task

                    def delete_task(self, task_id: int) -> bool:
                    """Удаление задачи"""
                    task = self.get_task(task_id)
                    if task:
                    self.tasks.remove(task)
                    return True
                    return False

                    def toggle_task(self, task_id: int) -> Optional[Task]:
                    """Переключение статуса задачи"""
                    task = self.get_task(task_id)
                    if task:
                    task.toggle_complete()
                    return task

                    # ==================== VIEW (ПРЕДСТАВЛЕНИЕ) ====================

                    class TaskView(ABC):
                    """Абстрактный класс представления"""

                    @abstractmethod
                    def display_tasks(self, tasks: List[Task]):
                    """Отображение списка задач"""
                    pass

                    @abstractmethod
                    def display_message(self, message: str):
                    """Отображение сообщения"""
                    pass

                    @abstractmethod
                    def get_input(self, prompt: str) -> str:
                    """Получение ввода от пользователя"""
                    pass

                    class ConsoleView(TaskView):
                    """Консольное представление"""

                    def display_tasks(self, tasks: List[Task]):
                    """Отображение списка задач в консоли"""
                    if not tasks:
                    print("📭 Задачи отсутствуют")
                    return

                    print(f"📋 Список задач ({len(tasks)}):")
                    print("-" * 50)

                    for task in tasks:
                    print(f"  {task}")
                    if task.description:
                    print(f"     📄 {task.description}")
                    if task.completed:
                    print(f"     ✅ Завершена: {task.updated_at.strftime('%d.%m.%Y')}")

                    def display_message(self, message: str):
                    """Отображение сообщения в консоли"""
                    print(f"💡 {message}")

                    def get_input(self, prompt: str) -> str:
                    """Получение ввода от пользователя в консоли"""
                    return input(f"{prompt}: ").strip()

                    class WebView(TaskView):
                    """Веб-представление (заглушка для демонстрации)"""

                    def display_tasks(self, tasks: List[Task]):
                    """Отображение списка задач в веб-интерфейсе"""
                    print("
                        ")
                        for task in tasks:
                        status = "completed" if task.completed else "pending"
                        print(f"  
                            ")
                            print(f"    {task.title}")
                            print(f"    {task.description}")
                            print(f"
                        ")
                        print("
                    ")

                    def display_message(self, message: str):
                    """Отображение сообщения в веб-интерфейсе"""
                    print(f"{message}")

                    def get_input(self, prompt: str) -> str:
                    """Получение ввода от пользователя в веб-интерфейсе"""
                    return f""

                    # ==================== CONTROLLER (КОНТРОЛЛЕР) ====================

                    class TaskController:
                    """Контроллер для управления задачами"""

                    def __init__(self, model: TaskModel, view: TaskView):
                    self.model = model
                    self.view = view
                    self.running = True

                    def run(self):
                    """Запуск приложения"""
                    self.view.display_message("Добро пожаловать в Todo приложение!")

                    while self.running:
                    self.show_menu()
                    choice = self.view.get_input("Выберите действие")
                    self.process_choice(choice)

                    def show_menu(self):
                    """Отображение меню"""
                    print("\n" + "=" * 50)
                    print("МЕНЮ TODO ПРИЛОЖЕНИЯ:")
                    print("1. 📄 Показать все задачи")
                    print("2. ➕ Добавить задачу")
                    print("3. ✓ Завершить задачу")
                    print("4. ✏️  Редактировать задачу")
                    print("5. 🗑️  Удалить задачу")
                    print("6. 🔍 Показать активные задачи")
                    print("7. ✅ Показать завершенные задачи")
                    print("8. 🚪 Выйти")
                    print("=" * 50)

                    def process_choice(self, choice: str):
                    """Обработка выбора пользователя"""
                    try:
                    if choice == '1':
                    self.show_all_tasks()
                    elif choice == '2':
                    self.add_task()
                    elif choice == '3':
                    self.toggle_task()
                    elif choice == '4':
                    self.edit_task()
                    elif choice == '5':
                    self.delete_task()
                    elif choice == '6':
                    self.show_active_tasks()
                    elif choice == '7':
                    self.show_completed_tasks()
                    elif choice == '8':
                    self.exit()
                    else:
                    self.view.display_message("Неверный выбор")
                    except Exception as e:
                    self.view.display_message(f"Ошибка: {e}")

                    def show_all_tasks(self):
                    """Показать все задачи"""
                    tasks = self.model.get_all_tasks()
                    self.view.display_tasks(tasks)

                    def add_task(self):
                    """Добавить новую задачу"""
                    title = self.view.get_input("Введите заголовок задачи")
                    if not title:
                    self.view.display_message("Заголовок не может быть пустым")
                    return

                    description = self.view.get_input("Введите описание задачи (необязательно)")

                    priority_input = self.view.get_input("Приоритет (1-высокий, 2-средний, 3-низкий)")
                    try:
                    priority = int(priority_input) if priority_input else 2
                    if priority not in [1, 2, 3]:
                    priority = 2
                    except ValueError:
                    priority = 2

                    task = self.model.add_task(title, description, priority)
                    self.view.display_message(f"Задача '{title}' добавлена (ID: {task.id})")

                    def toggle_task(self):
                    """Завершить/возобновить задачу"""
                    tasks = self.model.get_all_tasks()
                    if not tasks:
                    self.view.display_message("Нет задач для изменения")
                    return

                    self.view.display_tasks(tasks)

                    try:
                    task_id = int(self.view.get_input("Введите ID задачи"))
                    task = self.model.toggle_task(task_id)

                    if task:
                    status = "завершена" if task.completed else "возобновлена"
                    self.view.display_message(f"Задача '{task.title}' {status}")
                    else:
                    self.view.display_message("Задача не найдена")
                    except ValueError:
                    self.view.display_message("Неверный ID задачи")

                    def edit_task(self):
                    """Редактировать задачу"""
                    tasks = self.model.get_all_tasks()
                    if not tasks:
                    self.view.display_message("Нет задач для редактирования")
                    return

                    self.view.display_tasks(tasks)

                    try:
                    task_id = int(self.view.get_input("Введите ID задачи для редактирования"))
                    task = self.model.get_task(task_id)

                    if not task:
                    self.view.display_message("Задача не найдена")
                    return

                    new_title = self.view.get_input(f"Новый заголовок [{task.title}]")
                    new_description = self.view.get_input(f"Новое описание [{task.description}]")
                    new_priority = self.view.get_input(f"Новый приоритет (1-3) [{task.priority}]")

                    # Обновляем только изменившиеся поля
                    updates = {}
                    if new_title:
                    updates['title'] = new_title
                    if new_description is not None:
                    updates['description'] = new_description
                    if new_priority:
                    try:
                    updates['priority'] = int(new_priority)
                    except ValueError:
                    pass

                    if updates:
                    self.model.update_task(task_id, **updates)
                    self.view.display_message(f"Задача '{task.title}' обновлена")
                    else:
                    self.view.display_message("Изменений нет")

                    except ValueError:
                    self.view.display_message("Неверный ID задачи")

                    def delete_task(self):
                    """Удалить задачу"""
                    tasks = self.model.get_all_tasks()
                    if not tasks:
                    self.view.display_message("Нет задач для удаления")
                    return

                    self.view.display_tasks(tasks)

                    try:
                    task_id = int(self.view.get_input("Введите ID задачи для удаления"))

                    confirm = self.view.get_input(f"Удалить задачу {task_id}? (y/N)")
                    if confirm.lower() == 'y':
                    if self.model.delete_task(task_id):
                    self.view.display_message(f"Задача {task_id} удалена")
                    else:
                    self.view.display_message("Задача не найдена")
                    else:
                    self.view.display_message("Удаление отменено")

                    except ValueError:
                    self.view.display_message("Неверный ID задачи")

                    def show_active_tasks(self):
                    """Показать активные задачи"""
                    tasks = self.model.get_tasks_by_status(False)
                    if tasks:
                    self.view.display_tasks(tasks)
                    else:
                    self.view.display_message("Нет активных задач")

                    def show_completed_tasks(self):
                    """Показать завершенные задачи"""
                    tasks = self.model.get_tasks_by_status(True)
                    if tasks:
                    self.view.display_tasks(tasks)
                    else:
                    self.view.display_message("Нет завершенных задач")

                    def exit(self):
                    """Выход из приложения"""
                    self.view.display_message("До свидания!")
                    self.running = False

                    # ==================== ФАСАД (ДОПОЛНИТЕЛЬНЫЙ ПАТТЕРН) ====================

                    class TodoAppFacade:
                    """Фасад для упрощенного взаимодействия с MVC"""

                    def __init__(self):
                    self.model = TaskModel()
                    self.view = ConsoleView()
                    self.controller = TaskController(self.model, self.view)

                    def run_simple(self):
                    """Упрощенный запуск приложения"""
                    print("🚀 Запуск Todo приложения (MVC архитектура)")

                    # Добавляем тестовые задачи
                    self.model.add_task("Изучить MVC", "Разобраться с паттерном Model-View-Controller", 1)
                    self.model.add_task("Написать код", "Реализовать MVC для Todo приложения", 2)
                    self.model.add_task("Протестировать", "Проверить работу всех компонентов", 3)

                    # Запускаем контроллер
                    self.controller.run()

                    # ==================== ИНИЦИАЛИЗАЦИЯ И ЗАПУСК ====================

                    def demo_mvc_workflow():
                    """Демонстрация работы MVC"""
                    print("=== ДЕМОНСТРАЦИЯ MVC АРХИТЕКТУРЫ ===\n")

                    # 1. Инициализация компонентов MVC
                    print("1. Инициализация компонентов MVC:")
                    model = TaskModel()
                    view = ConsoleView()
                    controller = TaskController(model, view)

                    print("   Model: создана")
                    print("   View: создана")
                    print("   Controller: создан")

                    # 2. Пользователь добавляет задачу
                    print("\n2. Пользователь добавляет задачу:")
                    print("   View: отображает форму ввода")
                    print("   Controller: обрабатывает ввод пользователя")
                    print("   Model: создает новую задачу")

                    task = model.add_task("Пример задачи", "Это тестовая задача", 2)
                    print(f"   Создана задача: {task}")

                    # 3. Пользователь просматривает задачи
                    print("\n3. Пользователь просматривает задачи:")
                    print("   Controller: запрашивает задачи у Model")
                    print("   Model: возвращает список задач")
                    print("   View: отображает задачи пользователю")

                    tasks = model.get_all_tasks()
                    view.display_tasks(tasks)

                    # 4. Пользователь завершает задачу
                    print("\n4. Пользователь завершает задачу:")
                    print("   Controller: обрабатывает запрос на завершение")
                    print("   Model: обновляет статус задачи")
                    print("   View: отображает обновленный список")

                    model.toggle_task(task.id)
                    tasks = model.get_all_tasks()
                    view.display_tasks(tasks)

                    print("\n✅ MVC архитектура работает корректно!")
                    print("   • Model управляет данными и логикой")
                    print("   • View отвечает за отображение")
                    print("   • Controller обрабатывает взаимодействие")

                    # ==================== ТОЧКА ВХОДА ====================

                    if __name__ == "__main__":
                    # Демонстрация работы MVC
                    demo_mvc_workflow()

                    print("\n" + "=" * 60)
                    print("ЗАПУСК ПОЛНОЦЕННОГО TODO ПРИЛОЖЕНИЯ")
                    print("=" * 60)

                    # Запуск приложения через фасад
                    app = TodoAppFacade()
                    app.run_simple()

                    print("\n🎉 MVC АРХИТЕКТУРА УСПЕШНО РЕАЛИЗОВАНА!")
                    print("Преимущества MVC:")
                    print("  • Разделение ответственности")
                    print("  • Упрощение тестирования")
                    print("  • Повторное использование кода")
                    print("  • Гибкость в изменении интерфейса")