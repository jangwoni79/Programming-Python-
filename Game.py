
for c in [str(x) for x in range(1, 99+1)]:  
    count = c.count('3') + c.count('6') + c.count('9')  
    if count:
        print('짝'*count)
    else:
        print(c)

#count는 리스트 내에 x가 몇 개 있는지 조사해서 그 개수를 돌려주는 함수