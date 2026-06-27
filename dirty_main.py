from datetime import datetime

from application.salary import *
from application.db.people import *


if __name__ == '__main__':
    current_date = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    print(f'Текущая дата и время: {current_date}')

    calculate_salary()
    get_employees()