## 두 개 뽑아서 더하기
# https://programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = []
    for i in range(len(numbers)) :
        for j in range(i+1, len(numbers)) :
            value = numbers[i] + numbers[j]
            if value not in answer:
                answer.append(value)
    answer.sort()
    return answer