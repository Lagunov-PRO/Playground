def list_of_months(start_month):
    """
    Создаёт циклический список из месяцев, начиная с заданного
    """
    start_month -= 1
    end_month = 12 + start_month
    months = [((month % 12) + 1) for month in range(start_month, end_month)]
    return months

