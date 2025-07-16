from datetime import datetime

def is_valid_date(date_text: str) -> bool:
    """
        Проверяет корректность и допустимость введённой даты.

        :param date_text: Дата в строковом формате YYYY-MM-DD.
        :return: True, если дата корректна и входит в допустимые пределы, иначе False.
    """
    try:
        date_obj = datetime.strptime(date_text, '%Y-%m-%d')
        min_date = datetime(1995, 6, 16)
        if date_obj < min_date or date_obj > datetime.now():
            return False
        return True
    except ValueError:
        return False