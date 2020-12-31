# https://programmers.co.kr/learn/courses/30/parts/12077

def solution2(genres, plays):
    # album = dict(zip(genres, plays)) # 중복 해결 안됨
    gen_list = []
    for i in range(len(genres)):
        print(genres[i])
        if genres[i] in gen_list:
            print("okay")
            print(type(genres[i]))
            genres[i][str(i)] = plays[i] # 아마도 문자열 슬라이싱 인식?
        else:
            gen_list.append(genres[i])
            print(type(genres[i]))
            genres[i] = {}
            genres[i][str(i)] = plays[i]
            print(genres[i])
    print(gen_list)
    answer = []
    return answer

def solution(genres, plays):
    genre_list = {}
    for i in range(len(genres)):
        genre_list[genres[i]] = '1'
    for j in range(len(genres)):
        genres[j][j] = plays[j]
        print(genres[j])
    answer = []
    return answer

def solution3(genres, plays):
    dic = {}
    for i in range(len(genres)):
        if genres[i] in dic.keys():
            temp = dic[genres[i]]
            temp[0] += plays[i]
            temp[1].append(i)
        else:
            dic[genres[i]] = [plays[i], [i]]



    print(dic)

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution2(genres, plays))