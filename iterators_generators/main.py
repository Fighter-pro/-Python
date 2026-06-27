
import types


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.flat_list = []
        self.index = 0

    def __iter__(self):
        self.flat_list = []
        self.index = 0
        self.flatten(self.list_of_list)
        return self

    def __next__(self):
        if self.index >= len(self.flat_list):
            raise StopIteration

        item = self.flat_list[self.index]
        self.index += 1
        return item

    def flatten(self, list_of_list):
        for item in list_of_list:
            if isinstance(item, list):
                self.flatten(item)
            else:
                self.flat_list.append(item)


def flat_generator(list_of_list):
    for item in list_of_list:
        if isinstance(item, list):
            for nested_item in flat_generator(item):
                yield nested_item
        else:
            yield item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == [
        'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None
    ]


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == [
        'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None
    ]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == [
        'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!'
    ]


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == [
        'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!'
    ]

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
    print('Все тесты пройдены')

