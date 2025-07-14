from datetime import datetime

def is_valid_date(date_text):
    try:
        date_obj = datetime.strptime(date_text, '%Y-%m-%d')
        min_date = datetime(1995, 6, 16)
        if date_obj < min_date or date_obj > datetime.now():
            return False
        return True
    except ValueError:
        return False