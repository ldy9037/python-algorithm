# 카카오 인턴십 - 1번 문제
def str_sort(str):
    sort_list = sorted(str)
    return "".join(sort_list)

def solution(survey, choices):
    answer = ''
    result = {}

    for order in ["RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA"]:
        order = str_sort(order)
        result[order] = {}
        for char in order: result[order][char] = 0
            

    for choice, question in zip(choices, survey):
        sorted_question = str_sort(question)

        score = choice - 4
        if score == 0: continue
        elif score < 0: result[sorted_question][question[0]] += abs(score)
        elif score > 0: result[sorted_question][question[1]] += abs(score)

    for k,v in result.items():
        answer += max(v,key=v.get)
        
    return answer

servey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]

print(solution(servey, choices))