# 단백질 바

# 고객이 원하는 단백질 바 함량(N)을 입력받는다.
N = int(input())

# divmod(나누어지는 수, 나누는 수) -> (몫, 나머지)인 튜플 형태로 값이 지정된 변수에 저장된다.
pure_protein = divmod(N, 250) # 입력된 단백질 바 함량(N)을 순수한 단백질 250g으로 나누어준 (몫, 나머지)
chicken = divmod(pure_protein[1], 40) # 순수한 단백질에서 구한 나머지를 닭가슴살 단백질 40g으로 나누어준 (몫, 나머지)
peanut = divmod(chicken[1], 10) # 닭가슴살에서 구한 나머지를 땅콩 단백질 10g으로 나누어준 (몫, 나머지)

if peanut[1] != 0: # 땅콩의 단백질 함량 10g으로 나누었을 때, 나머지가 0이 아니면 -1을 출력해준다.
    print(-1)
else: # 그렇지 않으면, 앞서 구한 고객이 원하는 단백질 바에 들어갈 최솟값의 경우를 출력해준다.
    print(pure_protein[0], chicken[0], peanut[0])