from code import get_total_distance

def test_get_total_distance():
    numbers_list = [3, 4, 4, 3, 2, 5, 1, 3, 3, 9, 3, 3]
    result = get_total_distance(numbers_list)
    assert result == 11 