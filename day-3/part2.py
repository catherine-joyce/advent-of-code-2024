import re
from sys import stdin

from part1 import get_multiples

def check_text_for_regex_includes_do_dont(text):
   result = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", text)
   return result

def get_total_multiples_includes_do_dont(expression):
    text_list = check_text_for_regex_includes_do_dont(expression)
    print(text_list)
    total = 0
    process_text = True
    for item in text_list:
        if item == "do()":
            process_text = True
        elif item == "don't()":
            process_text = False
        else:
            if process_text:
               total += get_multiples(item)
    return total

def get_input_and_total_including_do_dont():
    whole_string = ""
    total = 0
    for line in stdin:
        whole_string += line
    total += get_total_multiples_includes_do_dont(whole_string)
    return total


if __name__ == "__main__":
    result = get_input_and_total_including_do_dont()
    print(result)
