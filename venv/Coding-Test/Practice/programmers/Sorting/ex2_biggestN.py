# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    answer = ''
    check = {}
    i = 0
    for num in numbers.copy():
        numbers[i] = str(num)
        i += 1
    numbers.sort(key=lambda x:x*3, reverse=True)
    for i in numbers:
        answer += i
    answer = str(int(answer))
    return answer

# numbers	 = [6, 10, 2]
numbers	 = [3, 30, 34, 5, 9]
# numbers = [0, 0, 0, 0]
print(solution(numbers))
# print(numbers.sort())