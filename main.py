from datetime import datetime

from colorama import Fore, Style

from application.salary import calculate_salary
from application.db.people import get_employees


def print_current_date():
    current_date = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    print(Fore.GREEN + f'Текущая дата и время: {current_date}' + Style.RESET_ALL)


if __name__ == '__main__':
    print_current_date()
    calculate_salary()
    get_employees()