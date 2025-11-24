from sys import stdin

from part1 import getinput, create_lists, sort_list

def create_dictionary(first_list):
    dict = {}
    for i in range(len(first_list)):
        if first_list[i] not in dict:
            dict[first_list[i]] = 0
    return dict

def get_values_dictionary(dict, second_list):
    for i in range(len(second_list)):
        if second_list[i] in dict:
            dict[second_list[i]] += 1
    return dict

def get_similarity_score(dict, first_list):
    total = 0
    for i in range(len(first_list)):
        key = first_list[i]
        value = dict[key]
        num = key * value
        total += num
    return total

if __name__ == "__main__":
    result = getinput()
    left_list, right_list = create_lists(result)
    sorted_left_list = sort_list(left_list)
    sorted_right_list = sort_list(right_list)
    dict = create_dictionary(sorted_left_list)
    values_added_dict = get_values_dictionary(dict, sorted_right_list)
    print(values_added_dict)
    total = get_similarity_score(dict, sorted_left_list)
    print(total)
