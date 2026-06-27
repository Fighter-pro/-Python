
from datetime import datetime
from functools import wraps


def logger(path):

    def __logger(old_function):

        @wraps(old_function)
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)

            with open(path, 'a', encoding='utf-8') as log_file:
                log_file.write(
                    f'Дата и время: {datetime.now()}\n'
                    f'Имя функции: {old_function.__name__}\n'
                    f'Аргументы: args={args}, kwargs={kwargs}\n'
                    f'Результат: {result}\n'
                    f'{"-" * 50}\n'
                )

            return result

        return new_function

    return __logger


@logger('flat_generator.log')
def get_flat_list(list_of_lists):
    result = []

    for item_list in list_of_lists:
        for item in item_list:
            result.append(item)

    return result


if __name__ == '__main__':
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    print(get_flat_list(list_of_lists_1))

