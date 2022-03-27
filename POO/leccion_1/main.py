from ast import For
from turtle import position


def solution(S, C):
    S=S.split("\n")
    titles=S[0].split(",")
    if isinstance(C,str):
        C=[C]
    positions=[]
    for index in C:
        
        positions.append(titles.index(index))

    
    data=[]
    for values in S[1:]:
        data.append(int(values.split(",")[positions[0]]))
    maxi=max(data)
    return maxi
S='city,temp2,temp\nParis,7,-3\nDubai,4,-4\nPorto,-1,-2'
C="temp"
print(solution(S,C))