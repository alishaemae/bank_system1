def format_date(date_value):
    if date_value and hasattr(date_value, "strftime"):
        return date_value.strftime("%d.%m.%Y")
    return str(date_value)
