def solution(id_list, report_list, k):
    answer = [0 for i in range(len(id_list))]
    report_status = dict()

    for report in set(report_list):
        reporter, target = tuple(report.split())

        if not target in report_status: report_status[target] = []
        report_status[target].append(reporter)
    
    for target, reporter_list in report_status.items():
        if len(reporter_list) < k: continue

        for reporter in reporter_list: answer[id_list.index(reporter)] += 1

    return answer
    

id_list = ["con", "ryan"]
report_list = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

print(solution(id_list, report_list, k))