import re
from sys import stdin

def check_text_for_regex(text):
   result = re.findall(r"mul\(\d+,\d+\)", text)
   return result

def get_numbers_list(text):
    numbers_list = re.findall(r"\d+", text)
    for i in range(len(numbers_list)):
        numbers_list[i] = int(numbers_list[i])
    return numbers_list

def get_multiples(text):
    result = get_numbers_list(text)
    return result[0] * result[1]

def get_total_multiples(expression):
    text_list = check_text_for_regex(expression)
    total = 0
    for item in text_list:
        total += get_multiples(item)
    return total

def get_input_and_total():
    total = 0
    for line in stdin:
        total += get_total_multiples(line)
    return total

if __name__ == "__main__":
    result = get_input_and_total()
    print(result)
