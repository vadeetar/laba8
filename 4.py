Python
                         Копировать
                    """
                    TDD (Test-Driven Development) для калькулятора
                    Шаги TDD: 1. Написать тест, 2. Запустить тест (упадет), 3. Написать код, 4. Запустить тест (пройдет)
                    """

                    import unittest

                    # ==================== ШАГ 1: ПИШЕМ ТЕСТЫ ====================

                    class TestCalculator(unittest.TestCase):
                    """Тесты для калькулятора"""

                    def test_addition(self):
                    """Тест сложения"""
                    calc = Calculator()
                    self.assertEqual(calc.add(2, 3), 5)
                    self.assertEqual(calc.add(-1, 1), 0)
                    self.assertEqual(calc.add(0, 0), 0)

                    def test_subtraction(self):
                    """Тест вычитания"""
                    calc = Calculator()
                    self.assertEqual(calc.subtract(5, 3), 2)
                    self.assertEqual(calc.subtract(3, 5), -2)
                    self.assertEqual(calc.subtract(0, 0), 0)

                    def test_multiplication(self):
                    """Тест умножения"""
                    calc = Calculator()
                    self.assertEqual(calc.multiply(2, 3), 6)
                    self.assertEqual(calc.multiply(-2, 3), -6)
                    self.assertEqual(calc.multiply(0, 5), 0)

                    def test_division(self):
                    """Тест деления"""
                    calc = Calculator()
                    self.assertEqual(calc.divide(6, 3), 2)
                    self.assertEqual(calc.divide(5, 2), 2.5)
                    self.assertEqual(calc.divide(0, 5), 0)

                    def test_division_by_zero(self):
                    """Тест деления на ноль (должен вызывать исключение)"""
                    calc = Calculator()
                    with self.assertRaises(ValueError):
                    calc.divide(5, 0)

                    def test_power(self):
                    """Тест возведения в степень"""
                    calc = Calculator()
                    self.assertEqual(calc.power(2, 3), 8)
                    self.assertEqual(calc.power(5, 0), 1)
                    self.assertEqual(calc.power(0, 5), 0)

                    def test_square_root(self):
                    """Тест квадратного корня"""
                    calc = Calculator()
                    self.assertEqual(calc.square_root(9), 3)
                    self.assertEqual(calc.square_root(0), 0)

                    def test_square_root_negative(self):
                    """Тест квадратного корня из отрицательного числа"""
                    calc = Calculator()
                    with self.assertRaises(ValueError):
                    calc.square_root(-4)

                    # ==================== ШАГ 2: ПИШЕМ МИНИМАЛЬНУЮ РЕАЛИЗАЦИЮ ====================

                    class Calculator:
                    """Простой калькулятор"""

                    def add(self, a, b):
                    """Сложение"""
                    return a + b

                    def subtract(self, a, b):
                    """Вычитание"""
                    return a - b

                    def multiply(self, a, b):
                    """Умножение"""
                    return a * b

                    def divide(self, a, b):
                    """Деление"""
                    if b == 0:
                    raise ValueError("Деление на ноль невозможно")
                    return a / b

                    def power(self, base, exponent):
                    """Возведение в степень"""
                    return base ** exponent

                    def square_root(self, x):
                    """Квадратный корень"""
                    if x < 0:
                    raise ValueError("Квадратный корень из отрицательного числа")
                    return x ** 0.5

                    # ==================== ШАГ 3: ЗАПУСКАЕМ ТЕСТЫ ====================

                    if __name__ == "__main__":
                    print("=== ЗАПУСК TDD ТЕСТОВ ===")

                    # Создаем тестовый набор
                    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)

                    # Запускаем тесты
                    runner = unittest.TextTestRunner(verbosity=2)
                    result = runner.run(suite)

                    # Выводим статистику
                    print(f"\n=== СТАТИСТИКА ===")
                    print(f"Всего тестов: {result.testsRun}")
                    print(f"Провалено: {len(result.failures)}")
                    print(f"Ошибок: {len(result.errors)}")

                    if result.wasSuccessful():
                    print("✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ!")
                    else:
                    print("❌ ЕСТЬ НЕУДАВШИЕСЯ ТЕСТЫ")

                    # ==================== ШАГ 4: РЕФАКТОРИНГ И ДОБАВЛЕНИЕ ФУНКЦИОНАЛА ====================

                    class AdvancedCalculator(Calculator):
                    """Улучшенный калькулятор с дополнительными функциями"""

                    def __init__(self):
                    """Инициализация с историей операций"""
                    self.history = []

                    def _record_operation(self, operation, a, b, result):
                    """Запись операции в историю"""
                    self.history.append({
                    'operation': operation,
                    'operands': (a, b),
                    'result': result,
                    'timestamp': __import__('datetime').datetime.now()
                    })

                    def add(self, a, b):
                    """Сложение с записью в историю"""
                    result = super().add(a, b)
                    self._record_operation('add', a, b, result)
                    return result

                    def subtract(self, a, b):
                    """Вычитание с записью в историю"""
                    result = super().subtract(a, b)
                    self._record_operation('subtract', a, b, result)
                    return result

                    def multiply(self, a, b):
                    """Умножение с записью в историю"""
                    result = super().multiply(a, b)
                    self._record_operation('multiply', a, b, result)
                    return result

                    def divide(self, a, b):
                    """Деление с записью в историю"""
                    result = super().divide(a, b)
                    self._record_operation('divide', a, b, result)
                    return result

                    def get_history(self):
                    """Получение истории операций"""
                    return self.history

                    def clear_history(self):
                    """Очистка истории"""
                    self.history.clear()

                    def calculate_expression(self, expression):
                    """Вычисление математического выражения"""
                    # Простой парсер выражений
                    try:
                    result = eval(expression)  # Внимание: eval опасен в продакшене!
                    self._record_operation('expression', expression, None, result)
                    return result
                    except Exception as e:
                    raise ValueError(f"Неверное выражение: {e}")

                    # ==================== ТЕСТЫ ДЛЯ УЛУЧШЕННОГО КАЛЬКУЛЯТОРА ====================

                    class TestAdvancedCalculator(unittest.TestCase):
                    """Тесты для улучшенного калькулятора"""

                    def setUp(self):
                    """Настройка перед каждым тестом"""
                    self.calc = AdvancedCalculator()

                    def tearDown(self):
                    """Очистка после каждого теста"""
                    self.calc.clear_history()

                    def test_history_recording(self):
                    """Тест записи в историю"""
                    self.calc.add(2, 3)
                    self.calc.subtract(5, 2)

                    history = self.calc.get_history()
                    self.assertEqual(len(history), 2)
                    self.assertEqual(history[0]['operation'], 'add')
                    self.assertEqual(history[0]['result'], 5)

                    def test_clear_history(self):
                    """Тест очистки истории"""
                    self.calc.add(1, 2)
                    self.calc.clear_history()
                    self.assertEqual(len(self.calc.get_history()), 0)

                    def test_expression_calculation(self):
                    """Тест вычисления выражений"""
                    result = self.calc.calculate_expression("2 + 3 * 4")
                    self.assertEqual(result, 14)

                    history = self.calc.get_history()
                    self.assertEqual(history[0]['operation'], 'expression')

                    def test_invalid_expression(self):
                    """Тест неверного выражения"""
                    with self.assertRaises(ValueError):
                    self.calc.calculate_expression("2 + ")

                    # ==================== ИНТЕГРАЦИОННЫЕ ТЕСТЫ ====================

                    def integration_test():
                    """Интеграционный тест калькулятора"""
                    print("\n=== ИНТЕГРАЦИОННЫЙ ТЕСТ ===")

                    calc = AdvancedCalculator()

                    # Серия операций
                    operations = [
                    ("2 + 3", calc.add(2, 3)),
                    ("10 - 4", calc.subtract(10, 4)),
                    ("3 * 5", calc.multiply(3, 5)),
                    ("20 / 4", calc.divide(20, 4)),
                    ("2 ^ 3", calc.power(2, 3))
                    ]

                    # Проверка результатов
                    for expr, result in operations:
                    print(f"{expr} = {result}")

                    # Проверка истории
                    print(f"\nИстория операций ({len(calc.get_history())} записей):")
                    for i, entry in enumerate(calc.get_history(), 1):
                    print(f"{i}. {entry['operation']}: {entry['operands']} = {entry['result']}")

                    # Очистка истории
                    calc.clear_history()
                    print(f"\nПосле очистки: {len(calc.get_history())} записей")

                    # ==================== ЗАПУСК ВСЕХ ТЕСТОВ ====================

                    if __name__ == "__main__":
                    # Запуск unit тестов
                    print("=== UNIT ТЕСТЫ ===")
                    suite = unittest.TestLoader().loadTestsFromTestCase(TestAdvancedCalculator)
                    runner = unittest.TextTestRunner(verbosity=1)
                    runner.run(suite)

                    # Запуск интеграционного теста
                    integration_test()

                    print("\n✅ TDD ЦИКЛ ЗАВЕРШЕН: ТЕСТЫ → КОД → РЕФАКТОРИНГ → ТЕСТЫ")# Коммит Sun Jan 11 17:57:00 RTZ 2026
