from datetime import datetime, timedelta

def get_days_between_dates(date1_str: str, date2_str: str) -> int:
    """Вычисляет количество дней между двумя датами в формате 'YYYY-MM-DD'."""
    date1 = datetime.strptime(date1_str, "%Y-%m-%d")
    date2 = datetime.strptime(date2_str, "%Y-%m-%d")
    return abs((date2 - date1).days)

def add_days_to_date(date_str: str, days: int) -> str:
    """Добавляет указанное количество дней к дате."""
    date = datetime.strptime(date_str, "%Y-%m-%d")
    new_date = date + timedelta(days=days)
    return new_date.strftime("%Y-%m-%d")

def is_leap_year(year: int) -> bool:
    """Проверяет, является ли год високосным."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)