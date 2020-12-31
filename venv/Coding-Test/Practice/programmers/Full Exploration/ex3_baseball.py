# https://programmers.co.kr/learn/courses/30/lessons/42841

def solution(baseball):
    # 가능한 모든 경우#각각서로다른 수
    from itertools import permutations
    can_list = []
    for i in permutations('123456789', 3):
        can_list.append(''.join(i))
        # print(''.join(i))

    # 안되는 경우 리스트로 뽑는다
    def func(arr, can_list):
        a = str(arr[0]);
        x_list = []
        for num in can_list:
            s = 0; # 스트라이크
            b = 0; # 볼
            if a[1] == num[1]:
                s += 1
            elif a[1] == num[2]:
                b += 1
            elif a[1] == num[0]:
                b += 1
            if a[2] == num[2]:
                s += 1
            elif a[2] == num[0]:
                b += 1
            elif a[2] == num[1]:
                b += 1
            if a[0] == num[0]:
                s += 1
            elif a[0] == num[1]:
                b += 1
            elif a[0] == num[2]:
                b += 1
            if s != arr[1] or b != arr[2]:
                x_list.append(num)
        return x_list

    # (모두) - (안돼) = (돼)
    set_list = set(can_list.copy())
    print(type(can_list))
    for arr in baseball:
        set_list -= set(func(arr, can_list))
    return len(set_list)

baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
print(solution(baseball))