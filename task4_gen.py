import types

def flatten(list_of_list, new_list=[]):
    for el in list_of_list:
        if isinstance(el, list):
            flatten(el, new_list)
        else:
            new_list.append(el)
    return new_list

def flat_generator(list_of_list):
    flat_list = flatten(list_of_list, new_list=[])
    count = 0
    while count < len(flat_list):
        yield flat_list[count]
        count += 1

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

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()
