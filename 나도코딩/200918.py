# # +추가 클래스 개념 정리
#
# 예를 들어 Person 클래스가 존재한다고 쳤을 때,
# name, age, skills 는 속성(인스턴스 변수)가 된다.
# 그리고 __init__, walk(), talk(), eat()... 등등은 행위(메소드)가 된다.
# 이제 Person 클래스를 가진 Person 인스턴스를 만들어보자.
# name = "somin", age=24, skills = "eating"
# name = "keunhwa", age=28, skills = "coding"
# ...등등 여러개의 인스턴스를 만들 수 있다.
#
# 즉 클래스는 설계도, 인스턴스는 설계또로부터 만들어진 개별적인 객체
#
# class Cat:
#     def meow(self): # 인스턴스 변수와 메소드 구현
#         print("야옹")
#
# cat1 = Cat() # Cat 인스턴스 생성 cat1이 이를 참조함
# cat1.meow() # Cat이 구현한 메소드 호출
#
# 인스턴스 변수 생성
#
# 현재 Cat 클래스에 대한 아무런 속성(인스턴스 변수)이 없으므로 변수를 생성해야함
# class Cat:
#     def __init__(self, name, color): # 생성자 함수 (인스턴스 생성시 자동으로 호출)
#         self.name = name
#         self.color = color
#     def info(self):
#         print("고양이 이름은 {0} 색깔은 {1}".format(name, color))


# Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오

# Answer)

# class House:
#     # 매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year
#     # 매물 정보 표시
#     def show_detail(self):
#         print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)
#
# house = []
# h1 = House("강남", "오피스텔", "매매", "10억", "2010년")
# h2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# h3 = House("송파", "빌라", "월세", "500/50", "2000년")
#
# house.append(h1)
# house.append(h2)
# house.append(h3)
#
# print("총 {0}대의 매물이 있습니다.".format(len(house)))
# for h in house:
#     h.show_detail()


# 예외처리
# try:
#     print("나누기")
#     num1 = int(input("첫번째 숫자 : "))
#     num2 = int(input("두번째 숫자 : "))
#     print("{0} / {1} = {2}".format(num1,num2, int(num1/num2)))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except:
#     print("에러 발생")


# 에러 발생시키기 -> 의도적으로 특정 에러를 발생시키는 것
# try:
#     print("한 자리 숫자 나누기")
#     num1 = int(input("첫 번째 숫자: "))
#     num2 = int(input("두 번째 숫자: "))
#     if num1 >= 10 or num2 >=10:
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")


# Quiz) 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오

# Answer)
# chicken = 10
# waiting = 1
# class SoldOutError(Exception):
#     pass
# try:
#     while(True):
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까? "))
#         if order > chicken:
#             print("재료가 부족합니다.")
#         elif order <= 0:
#             raise ValueError
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."\
#                   .format(waiting, order))
#             waiting += 1
#             chicken -= order
#         if chicken <= 0:
#             raise SoldOutError
# except ValueError:
#     print("잘못된 값을 입력하였습니다.")
# except SoldOutError:
#     print("재고가 소진되어 더이상 주문을 받지 않습니다.")


# 패키지 : 모듈들의 합
# import 사용시 주의사항
# import ㅁㅁ.ㅇㅇ 부분에서 점(.) 뒤의 ㅇㅇ부분은 모듈이나 패키지만 가능
# 클래스나 함수는 import를 바로 직접적으로 할 수 없음
# 하지만! from ㅁㅁ.ㅇㅇ import ㅂㅂ 에서는 ㅂㅂ에 클래스 사용 가능


# Quiz) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오

# Answer)
# import byme
# byme.sign()