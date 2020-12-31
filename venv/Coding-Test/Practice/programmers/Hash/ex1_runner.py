# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, z in zip(participant, completion):
        if p != z:
            answer = p
            break
        else:
            answer = participant[-1]
    return answer

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
participant.sort()
completion.sort()
print(participant)
print(completion)
print(solution(participant, completion))
