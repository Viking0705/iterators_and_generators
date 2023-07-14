class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def flatten(self, list_of_list, new_list=[]):
        for el in list_of_list:
            if isinstance(el, list):
                self.flatten(el,new_list)
            else:
                new_list.append(el)
        return new_list
    
    def __iter__(self):
        self.flat_list = self.flatten(self.list_of_list, new_list=[])
        self.counter = -1
        return self
    
    def __next__(self):
        self.counter += 1
        if self.counter >= len(self.flat_list):
            raise StopIteration
        item = self.flat_list[self.counter]
        return item


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

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()