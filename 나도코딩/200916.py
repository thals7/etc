# while -> 어떤 조건을 만족할때까지 반복

# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0 :
#         print("커피는 폐기처분되었습니다.")

# customer = "토르"
# person = "Unknown"
# while person != customer:
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")


# 한 줄 for

# 출석번호가 1 2 3 4, 앞에 100 붙이기로 함 -> 101 102 103 104
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# 학생 이름을 길이로 변환
# students = ["아이언맨", "토르", "아이엠 그루트"]
# students = [len(i) for i in students]
# print(students)

# 학생 이름을 대문자로 변환
# students = ["Iron man","Thor","I am groot"]
# students = [i.upper() for i in students]
# print(students)


# Quiz) 총 탑승 승객 수를 구하는 프로그램

# Answer)
# from random import *
# count = 0
# for i in range(1,51):
#     time = randint(5,50)
#     if time <=15:
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         count += 1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
# print("총 탑승 승객 : %d 분" %count)


# 함수
# # 전달값과 반환값
# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance + money
#
# balance = 0
# balance = deposit(balance, 1000)
# print(balance)

# 함수 가변인자
# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()
# profile("유재석", 20, "Python", "Java")

# 지역변수 전역변수
# gun = 10
# def checkpoint(soldiers):
#     gun = 20
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}.format(gun)")
#
# print("전체 총 : {0}".format(gun)) -> 이때는 gun 이 함수 밖의 변수로 10이 나옴
# checkpoint(2) -> 이때는 gun이 checkpoint 함수 안의 gun으로 18이 나옴
# 따라서 이것을 전역변수로 바꾸어서 함수 밖과 안에서 통일해줘야함 -> global 지역변수
# gun = 10
# def checkpoint(soldiers):
#     global gun
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}.format(gun)")


# Quiz) 표준 체중을 구하는 프로그램을 작성하시오

# Answer)
# def std_weight(height, gender):
#     if gender == "남자":
#         return height*height*22
#     elif gender == "여자":
#         return height*height*21
#
# height = 175
# gender = "남자"
# weight = round(std_weight(height/100, gender),2)
# print("키 {0}cm {1}의 표준 체중은 {2}입니다.".format(height,gender,weight))


# 파일입출력
# score_file = open("score.txt", "w", encoding="utf8")
## w는 쓰기 용도(덮어쓰기) a는 이어쓰기 r은 읽기용도
# utf8 을 써주는 이유는 한글 파일을 읽을때 저게없으면 오류가 날 수 있어서
# printf("수학 : 0", file=score_file)
# printf("영어 : 50",file=score_file)
# score_file.close()
#
# score_file = open("score.txt","r", encoding="utf8")
# print(score_file.read())
# score_file.close()


# pickle 텍스트 이외의 자료형(리스트나 클래스 등)을 파일로 저장하기 위하여 쓰는 모듈
# import pickle
# profile_file = open("profile.pickle","wb")
# # wb는 피클파일의 쓰기용도 피클에서는 따로 인코딩은 필요없음
# profile = {"이름":"정소민", "나이":24, "취미":["먹기","자기"]}
# print(profile)
# pickle.dump(profile, profile_file)
# # profile 에 있는 정보를 file에 저장
# profile_file.close()