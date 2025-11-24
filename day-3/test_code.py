from part1 import check_text_for_regex, get_numbers_list, get_multiples, get_total_multiples

def test_one_matching_expression():
    expression = "mul(1,4)"
    result = check_text_for_regex(expression)
    assert result == ["mul(1,4)"]

def test_second_matching_expression():
    expression = "mul(123,4)"
    result = check_text_for_regex(expression)
    assert result == ["mul(123,4)"]

def test_multiple_matching_expressions_text():
    expression = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)"
    result = check_text_for_regex(expression)
    assert result == ["mul(2,4)", "mul(5,5)"]

def test_get_numbers():
    text = "mul(123,4)"
    result = get_numbers_list(text)
    assert result == [123, 4]

def test_get_multiples():
    text = "mul(123,4)"
    total = get_multiples(text)
    assert total == 492

def test_get_total_multiples():
    expression = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)"
    total = get_total_multiples(expression)
    assert total == 33

def test_second_get_total_multiples():
    expression = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    total = get_total_multiples(expression)
    assert total == 161