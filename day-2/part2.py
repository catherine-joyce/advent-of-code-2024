from part1 import get_input

def report_safety_check(report):
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
    
def check_report_safety_part_2(report):
    if report_safety_check(report):
        return True
    else:
        if tolerance_safety_check(report):
            return True
        else: 
            return False
        
def tolerance_safety_check(report):
    safe_report_num = 0 
    for i in range(len(report)):
        report_instance = report.copy()
        report_instance.pop(i)
        if report_safety_check(report_instance):
            safe_report_num += 1
    if safe_report_num >= 1:
        return True
    else: 
        return False
    
        
def check_all_reports(reports_list):
    safe_report_count = 0
    for report in reports_list:
        if check_report_safety_part_2(report):
            safe_report_count += 1
    return safe_report_count


if __name__ == "__main__":
    result = get_input()
    print(result)
    num_safe_reports = check_all_reports(result)
    print(num_safe_reports)