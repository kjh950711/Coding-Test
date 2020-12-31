# https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    first_len = len(clothes)
    dict = {}
    for cloth in clothes:
        if cloth[1] in dict.keys():
            if str(type(dict[cloth[1]])) == "<class 'list'>":
                # print("들어옴")
                list = dict[cloth[1]]
                # print(type(list), list)
                # print(list.append(cloth[0]))
                list.append(cloth[0])
                dict[cloth[1]] = list
            else:
                dict[cloth[1]] = [dict[cloth[1]], cloth[0]]
        else:
            dict[cloth[1]] = cloth[0]
        print(dict)
    print(dict)
    answer = 1
    for key in dict.keys():
        if str(type(dict[key])) == "<class 'list'>":
            num = len(dict[key]) + 1
        else:
            num = 2
        answer = answer * num
    # print(answer)
    return answer - 1

# clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))
# print(len(clothes))
# print(type(clothes))