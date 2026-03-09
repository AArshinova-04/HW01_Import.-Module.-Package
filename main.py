from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    # Выводим текущую дату и время
    print(f"Текущая дата: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Вызов функций
    calculate_salary(120000.00)
    get_employees('Ivanov')