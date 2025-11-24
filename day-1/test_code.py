from part1 import create_lists, sort_list, get_total_distance

from part2 import create_dictionary, get_values_dictionary, get_similarity_score

def test_create_lists():
    numbers_list = [3, 4, 4, 3, 2, 5, 1, 3, 3, 9, 3, 3]
    first_list, second_list = create_lists(numbers_list)
    assert first_list == [3, 4, 2, 1, 3, 3] 
    assert second_list == [4, 3, 5, 3, 9, 3]

def test_sort_list():
    first_list = [3, 4, 2, 1, 3, 3]
    sorted_list = sort_list(first_list)
    assert sorted_list == [1, 2, 3, 3, 3, 4]

def test_get_total_distance():
    first_list = [1, 2, 3, 3, 3, 4]
    second_list = [3, 3, 3, 4, 5, 9]
    total = get_total_distance(first_list, second_list)
    assert total == 11

def test_create_dictionary():
    first_list = [1, 2, 3, 3, 3, 4]
    dict = create_dictionary(first_list)
    assert dict == {1: 0, 2: 0, 3: 0, 4: 0}

def test_get_values_dictionary():
    dict = {1: 0, 2: 0, 3: 0, 4: 0}
    second_list = [3, 3, 3, 4, 5, 9]
    values_dict = get_values_dictionary(dict, second_list)
    assert values_dict == {1: 0, 2: 0, 3: 3, 4: 1}

def test_get_similarity_score():
    dict = {1: 0, 2: 0, 3: 3, 4: 1}
    first_list = [1, 2, 3, 3, 3, 4]
    total = get_similarity_score(dict, first_list)
    assert total == 31