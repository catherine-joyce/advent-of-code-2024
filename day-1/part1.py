from sys import stdin

def getinput():
    return list(map(int, stdin.read().split()))

def create_lists(input_list):
    left_list = []
    right_list = []
    for i in range(len(input_list)):
        if i % 2 == 0:
            left_list.append(input_list[i])
        else:
            right_list.append(input_list[i])
    return left_list, right_list

def sort_list(numbers_list):
    numbers_list.sort()
    return numbers_list

def get_total_distance(first_list, second_list):
    total_distance = 0
    for i in range(len(first_list)):
        if first_list[i] > second_list[i]:
           distance = first_list[i] - second_list[i]
        elif first_list[i] < second_list[i]:
           distance = second_list[i] - first_list[i]
        else:
            distance = 0
        total_distance += distance
    return total_distance

if __name__ == "__main__":
    result = getinput()
    left_list, right_list = create_lists(result)
    total_distance = get_total_distance(sort_list(left_list), sort_list(right_list))
    print(total_distance)
