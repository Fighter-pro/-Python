
class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)


def check_brackets(brackets_string):
    stack = Stack()

    brackets_pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    opening_brackets = '([{'
    closing_brackets = ')]}'

    for bracket in brackets_string:
        if bracket in opening_brackets:
            stack.push(bracket)

        elif bracket in closing_brackets:
            if stack.is_empty():
                return 'Несбалансированно'

            last_opening_bracket = stack.pop()

            if last_opening_bracket != brackets_pairs[bracket]:
                return 'Несбалансированно'

    if stack.is_empty():
        return 'Сбалансированно'

    return 'Несбалансированно'


def test_brackets():
    balanced_sequences = [
        '(((([{}]))))',
        '[([])((([[[]]])))]{()}',
        '{{[()]}}'
    ]

    unbalanced_sequences = [
        '}{',
        '{{[(])]}',
        '[[{())}]'
    ]

    for sequence in balanced_sequences:
        assert check_brackets(sequence) == 'Сбалансированно'

    for sequence in unbalanced_sequences:
        assert check_brackets(sequence) == 'Несбалансированно'


if __name__ == '__main__':
    test_brackets()

    brackets_string = input('Введите строку со скобками: ')
    print(check_brackets(brackets_string))
