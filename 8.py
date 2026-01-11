Python
                         Копировать
                    import argparse
                    import sys
                    import os
                    from datetime import datetime

                    # 1. Основной парсер
                    def create_parser():
                    """Создание парсера аргументов командной строки"""
                    parser = argparse.ArgumentParser(
                    description="Универсальное CLI приложение",
                    epilog="Примеры использования:\n"
                    "  python app.py greet --name Вадим\n"
                    "  python app.py calculate --operation add 10 5\n"
                    "  python app.py file --action info README.md",
                    formatter_class=argparse.RawDescriptionHelpFormatter
                    )

                    # Основные аргументы
                    parser.add_argument(
                    '--version',
                    action='version',
                    version='CLI App 1.0.0'
                    )
                    parser.add_argument(
                    '--verbose',
                    action='store_true',
                    help='подробный вывод'
                    )

                    # Подкоманды
                    subparsers = parser.add_subparsers(
                    dest='command',
                    title='доступные команды',
                    help='выберите команду'
                    )

                    # Команда greet
                    add_greet_parser(subparsers)

                    # Команда calculate
                    add_calculate_parser(subparsers)

                    # Команда file
                    add_file_parser(subparsers)

                    # Команда system
                    add_system_parser(subparsers)

                    return parser

                    # 2. Парсер для команды greet
                    def add_greet_parser(subparsers):
                    """Парсер для команды приветствия"""
                    parser_greet = subparsers.add_parser(
                    'greet',
                    help='приветствие пользователя',
                    description='Выводит приветственное сообщение'
                    )

                    parser_greet.add_argument(
                    '--name',
                    required=True,
                    help='имя пользователя'
                    )
                    parser_greet.add_argument(
                    '--formal',
                    action='store_true',
                    help='формальное приветствие'
                    )
                    parser_greet.add_argument(
                    '--repeat',
                    type=int,
                    default=1,
                    help='количество повторений'
                    )

                    # 3. Парсер для команды calculate
                    def add_calculate_parser(subparsers):
                    """Парсер для математических операций"""
                    parser_calc = subparsers.add_parser(
                    'calculate',
                    help='математические операции',
                    description='Выполняет математические операции'
                    )

                    parser_calc.add_argument(
                    '--operation',
                    choices=['add', 'sub', 'mul', 'div', 'pow', 'sqrt'],
                    required=True,
                    help='тип операции'
                    )
                    parser_calc.add_argument(
                    'numbers',
                    nargs='+',
                    type=float,
                    help='числа для операции (для sqrt нужно одно число)'
                    )
                    parser_calc.add_argument(
                    '--precision',
                    type=int,
                    default=2,
                    help='точность вычислений'
                    )

                    # 4. Парсер для команды file
                    def add_file_parser(subparsers):
                    """Парсер для работы с файлами"""
                    parser_file = subparsers.add_parser(
                    'file',
                    help='операции с файлами',
                    description='Выполняет операции с файлами'
                    )

                    parser_file.add_argument(
                    '--action',
                    choices=['info', 'read', 'write', 'delete', 'list'],
                    required=True,
                    help='действие с файлом'
                    )
                    parser_file.add_argument(
                    'filename',
                    nargs='?',
                    help='имя файла (не требуется для list)'
                    )
                    parser_file.add_argument(
                    '--content',
                    help='содержимое для записи (только для write)'
                    )

                    # 5. Парсер для команды system
                    def add_system_parser(subparsers):
                    """Парсер для системной информации"""
                    parser_system = subparsers.add_parser(
                    'system',
                    help='системная информация',
                    description='Показывает информацию о системе'
                    )

                    parser_system.add_argument(
                    '--info',
                    choices=['all', 'python', 'os', 'time'],
                    default='all',
                    help='тип информации'
                    )

                    # 6. Обработчики команд
                    def handle_greet(args):
                    """Обработчик команды greet"""
                    greeting = "Здравствуйте" if args.formal else "Привет"

                    for i in range(args.repeat):
                    if args.verbose:
                    time = datetime.now().strftime("%H:%M:%S")
                    print(f"[{time}] {greeting}, {args.name}!")
                    else:
                    print(f"{greeting}, {args.name}!")

                    def handle_calculate(args):
                    """Обработчик команды calculate"""
                    from math import sqrt

                    operation = args.operation
                    numbers = args.numbers
                    precision = args.precision

                    if args.verbose:
                    print(f"Операция: {operation}")
                    print(f"Числа: {numbers}")

                    try:
                    if operation == 'add':
                    result = sum(numbers)
                    op_symbol = '+'
                    elif operation == 'sub':
                    result = numbers[0] - sum(numbers[1:])
                    op_symbol = '-'
                    elif operation == 'mul':
                    result = 1
                    for num in numbers:
                    result *= num
                    op_symbol = '×'
                    elif operation == 'div':
                    if len(numbers) != 2:
                    raise ValueError("Для деления нужно ровно два числа")
                    if numbers[1] == 0:
                    raise ValueError("Деление на ноль невозможно")
                    result = numbers[0] / numbers[1]
                    op_symbol = '÷'
                    elif operation == 'pow':
                    if len(numbers) != 2:
                    raise ValueError("Для возведения в степень нужно ровно два числа")
                    result = numbers[0] ** numbers[1]
                    op_symbol = '^'
                    elif operation == 'sqrt':
                    if len(numbers) != 1:
                    raise ValueError("Для квадратного корня нужно одно число")
                    if numbers[0] < 0:
                    raise ValueError("Квадратный корень из отрицательного числа")
                    result = sqrt(numbers[0])
                    op_symbol = '√'

                    # Форматируем результат
                    if isinstance(result, float):
                    result_str = f"{result:.{precision}f}"
                    else:
                    result_str = str(result)

                    print(f"Результат: {result_str}")

                    except ValueError as e:
                    print(f"Ошибка: {e}", file=sys.stderr)
                    sys.exit(1)

                    def handle_file(args):
                    """Обработчик команды file"""
                    action = args.action

                    if action == 'list':
                    files = os.listdir('.')
                    print(f"Файлы в текущей директории ({len(files)}):")
                    for file in sorted(files):
                    if os.path.isfile(file):
                    size = os.path.getsize(file)
                    print(f"  {file} ({size} байт)")
                    return

                    if not args.filename:
                    print("Ошибка: укажите имя файла", file=sys.stderr)
                    sys.exit(1)

                    filename = args.filename

                    try:
                    if action == 'info':
                    if not os.path.exists(filename):
                    print(f"Файл {filename} не существует", file=sys.stderr)
                    sys.exit(1)

                    stat = os.stat(filename)
                    created = datetime.fromtimestamp(stat.st_ctime)
                    modified = datetime.fromtimestamp(stat.st_mtime)

                    print(f"Информация о файле {filename}:")
                    print(f"  Размер: {stat.st_size} байт")
                    print(f"  Создан: {created.strftime('%Y-%m-%d %H:%M:%S')}")
                    print(f"  Изменен: {modified.strftime('%Y-%m-%d %H:%M:%S')}")

                    elif action == 'read':
                    if not os.path.exists(filename):
                    print(f"Файл {filename} не существует", file=sys.stderr)
                    sys.exit(1)

                    with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()

                    print(f"Содержимое файла {filename}:")
                    print("-" * 40)
                    print(content)
                    print("-" * 40)

                    elif action == 'write':
                    content = args.content or input("Введите содержимое файла: ")

                    with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)

                    print(f"Файл {filename} записан")

                    elif action == 'delete':
                    if not os.path.exists(filename):
                    print(f"Файл {filename} не существует", file=sys.stderr)
                    sys.exit(1)

                    confirm = input(f"Удалить файл {filename}? (y/N): ")
                    if confirm.lower() == 'y':
                    os.remove(filename)
                    print(f"Файл {filename} удален")
                    else:
                    print("Удаление отменено")

                    except Exception as e:
                    print(f"Ошибка: {e}", file=sys.stderr)
                    sys.exit(1)

                    def handle_system(args):
                    """Обработчик команды system"""
                    info_type = args.info

                    print("Системная информация:")
                    print("=" * 40)

                    if info_type in ['all', 'python']:
                    print("Python:")
                    print(f"  Версия: {sys.version}")
                    print(f"  Исполняемый файл: {sys.executable}")
                    print()

                    if info_type in ['all', 'os']:
                    print("ОС:")
                    print(f"  Платформа: {sys.platform}")
                    print(f"  Кодировка: {sys.getdefaultencoding()}")
                    print(f"  Текущая директория: {os.getcwd()}")
                    print()

                    if info_type in ['all', 'time']:
                    now = datetime.now()
                    print("Время:")
                    print(f"  Текущее: {now.strftime('%Y-%m-%d %H:%M:%S')}")
                    print(f"  Таймстамп: {now.timestamp():.0f}")

                    # 7. Основная функция
                    def main():
                    """Основная функция приложения"""
                    parser = create_parser()
                    args = parser.parse_args()

                    if args.verbose:
                    print(f"Запуск команды: {args.command}")
                    print(f"Аргументы: {args}")

                    if not args.command:
                    parser.print_help()
                    return

                    # Вызываем соответствующий обработчик
                    handlers = {
                    'greet': handle_greet,
                    'calculate': handle_calculate,
                    'file': handle_file,
                    'system': handle_system
                    }

                    handler = handlers.get(args.command)
                    if handler:
                    try:
                    handler(args)
                    except KeyboardInterrupt:
                    print("\nПрервано пользователем")
                    sys.exit(0)
                    else:
                    print(f"Неизвестная команда: {args.command}", file=sys.stderr)
                    sys.exit(1)

                    # 8. Пример использования
                    if __name__ == "__main__":
                    # Тестирование разных команд

                    # Команда 1: Приветствие
                    print("=== Команда greet ===")
                    sys.argv = ["app.py", "greet", "--name", "Вадим", "--formal"]
                    main()

                    print("\n=== Команда calculate ===")
                    # Команда 2: Вычисление
                    sys.argv = ["app.py", "calculate", "--operation", "add", "10", "20", "30"]
                    main()

                    print("\n=== Команда file ===")
                    # Команда 3: Информация о файле
                    if os.path.exists("README.md"):
                    sys.argv = ["app.py", "file", "--action", "info", "README.md"]
                    main()

                    print("\n=== Команда system ===")
                    # Команда 4: Системная информация
                    sys.argv = ["app.py", "system", "--info", "python"]
                    main()

                    # 9. Дополнительные возможности argparse
                    # - Вложенные подкоманды
                    # - Взаимоисключающие аргументы
                    # - Группы аргументов
                    # - Кастомные типы
                    # - Парсинг из файла конфигурации
                    # - Автодополнение в bash