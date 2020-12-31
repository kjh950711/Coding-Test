# https://programmers.co.kr/learn/courses/30/parts/12077

def solution(genres, plays):
    dic = {}
    for idx, genre in enumerate(genres):
        if genre in dic.keys():
            temp = dic[genre]
            temp['sum'] += plays[idx]
            temp['plays'][idx] = plays[idx]
        else:
            dic[genre] = {'sum':plays[idx], 'plays':{idx : plays[idx]}}
    print(dic)
    print(dic.items())

    result = []
    for k, v in sorted(dic.items(), key=lambda dic: dic[1]['sum'], reverse=True):
        plays_dic = v['plays']
        print(plays_dic)
        for idx, plays in sorted(plays_dic.items(), key=lambda plays_dic: plays_dic[1], reverse=True)[:2]:
            result.append(idx)

    return result

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))