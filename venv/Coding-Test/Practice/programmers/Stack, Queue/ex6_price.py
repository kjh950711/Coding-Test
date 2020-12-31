# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = []
    for i in range(len(prices)-2):
        time = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                time += 1
            else:
                time += 1
                break
        answer.append(time)
    answer.append(1)
    answer.append(0)
    # print("확인", answer)
    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))