# \n : 줄바꿈
# print("백문이 불여일견\n백견이 불여일타")

# \" \' : 문장 내에서 따옴표
# 저는 "나도코딩"입니다.
# print("저는 \"나도코딩"\입니다.")

# \\ : 문장 내에서 \

# \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine" -> 결과는 PineApple

# \b : 백스페이스(한글자 삭제)

# \t : 탭


# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# 규칙 1 : http:// 부분 제외 -> naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 -> naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
# ex) 생성된 비밂번호 : nav51!

# Answer
# A = input()
# B = A.replace("http://","")
# B = B[:B.index(".")]
# password = B[:3] + str(len(B)) + str(B.count("e")) + "!"
# print("{}의 비밀번호는 {}입니다.".format(A,password))



# list.pop() -> 맨 뒤의 목록 하나를 꺼냄

# list.sort() -> 오름차순 정렬
# list.reverse() -> 순서 뒤집어서 정렬

# list.clear() -> 모두 지우기

# 리스트 확장
# list_1.extend(list_2) -> list_1의 목록에 list_2의 목록까지 다 나옴



# 사전값을 가져오는 방법
# 1.print(dict[키]) -> 값 출력
# 2.print(dict.get(키)) -> 값 출력
# cf)사전에 없는 키를 입력했을 경우?
# []를 쓰면 에러를 뜨면서 종료 / get()을 쓰면 None이 뜨고 종료되지 않음
# 또는 get(키, "") 를 입력하면 값이 없을때 None 대신 ""안의 말이 출력됨

# print(dict.keys()) -> key들만 출력
# print(dict.values()) -> value들만 출력
# print(dict.items()) -> key, value 쌍으로 출력


# 집합(set)
# 중복 안됨, 순서 없음
# set = {1, 2, 3, 3}
# print(set) -> {1, 2, 3} (3 한번만 출력됨)

# 교집합
# A = {1, 2, 3} / B = {3, 4, 5}
# print(A & B) -> {3}
# print(A.intersection(B)) -> {3}

# 합집합
# print(A | B)
# print(A.union(B))

# 차집합
# print(A - B)
# print(A.difference(B))


# Quiz) 추첨 프로그램

# Answer)
from random import *
users = range(1,21)
users = list(users)
shuffle(users)

winners = sample(users, 4)

print(" -- 당첨자 발표 --")
print("치킨 당첨자 : {}".format(winners[0]))
print("커피 당첨자 : {}".format(winners[1:4]))
print(" -- 축하합니다 --")