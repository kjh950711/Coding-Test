# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    first = 0 # 수포자1 점수
    second = 0 # 수포자2 점수
    third = 0 # 수포자3 점수
    list2 = [1, 3, 4, 5]
    list3 = [3, 1, 2, 4, 5]
    two = 0
    three = 0
    for i in range(len(answers)):
        answer = answers[i]
        first_a = i%5 + 1

        if i%2 == 0:
            second_a = 2
            third_a = list3[three%5]
        else:
            second_a = list2[two%4]
            third_a = list3[three%5]
            two += 1
            three += 1
        if answer == first_a:
            first += 1
        if answer == second_a:
            second += 1
        if answer == third_a:
            third += 1
    score = [first, second, third]
    # print(person)
    max_val = max(score)
    top = []
    idx = 0
    for i in score:
        if i == max_val:
            top.append(idx + 1)
        idx += 1
    return top

# answers = [1,2,3,4,5]
# answers = [1,3,2,4,2]
answers = [0, 0, 0, 0, 0]
print(solution(answers))