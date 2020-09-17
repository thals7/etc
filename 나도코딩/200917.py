# Quiz) 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램 작성

# Answer)
# for i in range(1,51):
#     report = open("{}주차.txt".format(i), "w", encoding="utf8")
#     report.write("- %d 주차 주간보고 -\n부서\n이름 :\n업무 요약 : " %(i))
#     report.close()


# Class

# 일반 유닛
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
#
# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# 공격 유닛
# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damege
#
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#               .format(self.name, location, self.damage))
#
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# 클래스의 상속
# class Unit:
#   def __init__(self, name, hp, damage)
#       self.name = name
#       self.hp = hp
# class AttackUnit(Unit): -> AttackUnit 은 Unit 클래스를 상속받아 만들어졌다는 의미
#   def __init__(self, name, hp, damage):
#       Unit.__init__(self, name, hp)
#       self.damage = damege
# AttackUnit에서 따로 self.name 과 self.hp를 정의할 필요가 없음