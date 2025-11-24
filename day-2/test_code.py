from part1 import check_report_safety

from part2 import check_report_safety_part_2

def test_safe_report():
    report = [7, 6, 4, 2, 1]
    assert check_report_safety(report) == True

def test_unsafe_report():
    report = [1, 2, 7, 8, 9]
    assert check_report_safety(report) == False

def test_second_unsafe_report():
    report = [9, 7, 6, 2, 1]
    assert check_report_safety(report) == False

def test_third_unsafe_report():
    report = [1, 3, 2, 4, 5]
    assert check_report_safety(report) == False

def test_fourth_unsafe_report():
    report = [8, 6, 4, 4, 1]
    assert check_report_safety(report) == False

def test_second_safe_report():
    report = [1, 3, 6, 7, 9]
    assert check_report_safety(report) == True

def test_fifth_unsafe_report():
    report = [7, 6, 4, 2, 4]
    assert check_report_safety(report) == False


def test_safe_report_part_2():
    report = [7, 6, 4, 2, 1]
    assert check_report_safety_part_2(report) == True

def test_unsafe_report_part_2():
    report = [1, 2, 7, 8, 9]
    assert check_report_safety_part_2(report) == False

def test_second_unsafe_report_part_2():
    report = [9, 7, 6, 2, 1]
    assert check_report_safety_part_2(report) == False

def test_second_safe_report_part_2():
    report = [1, 3, 2, 4, 5]
    assert check_report_safety_part_2(report) == True

def test_third_safe_report_part_2():
    report = [8, 6, 4, 4, 1]
    assert check_report_safety_part_2(report) == True

def test_fourth_safe_report_part_2():
    report = [1, 3, 6, 7, 9]
    assert check_report_safety_part_2(report) == True
