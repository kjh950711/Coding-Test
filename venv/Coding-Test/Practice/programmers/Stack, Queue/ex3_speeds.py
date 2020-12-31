# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    while len(progresses) != 0:
        service = 0
        for i in range(len(speeds)):
            progresses[i] = progresses[i] + speeds[i]
        print(progresses)
        for progress in progresses:
            if progress >= 100:
                service += 1
            else: break
        for i in range(service):
            progresses.remove(progresses[0])
            speeds.remove(speeds[0])
        if not service == 0:
            answer.append(service)
    return answer

progresses = [93,30,55]
speeds = [1,30,5]
print(solution(progresses, speeds))

