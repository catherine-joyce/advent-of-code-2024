from sys import stdin

def get_input():
    total_list = []
    for line in stdin:
        total_list.append(list(map(int, line.split())))
    return total_list

def check_report_safety(report):
    if report[0] > report[1]:
        for i in range(len(report)-1):
            j = i + 1
            if (report[i] < report[j]):
                return False
            if abs(report[i] - report[j]) > 3 or abs(report[i] - report[j]) == 0:
                return False
        return True
    elif report[0] < report[1]:
        for i in range(len(report)-1):
            j = i + 1
            if (report[i] > report[j]):
                return False
            if abs(report[i] - report[j]) > 3 or abs(report[i] - report[j]) == 0:
                return False
        return True
    else:
        return False
        
def check_all_reports(reports_list):
    safe_report_count = 0
    for report in reports_list:
        if check_report_safety(report):
            safe_report_count += 1
    return safe_report_count


if __name__ == "__main__":
    result = get_input()
    print(result)
    num_safe_reports = check_all_reports(result)
    print(num_safe_reports)