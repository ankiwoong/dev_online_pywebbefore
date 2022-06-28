# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체 보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도 존재, 인스턴스 생성 후 사용

# 선언
# class 클래스명:
#     함수
#     함수
#     함수

# 예제1
class UserInfo:
    # 속성, 메소드
    def __init__(self, name, height, address):
        self.name = name
        self.height = height
        self.address = address

    def user_info_p(self):
        print("Name : ", self.name)
        print("height : ", self.height)
        print("address : ", self.address)


# 네임스페이스
user1 = UserInfo("park", 170, "서울시")
user1.user_info_p()

user2 = UserInfo("kim", 130, "대전시")
user2.user_info_p()

print(id(user1))
print(id(user2))
print(user1.__dict__)
print(user2.__dict__)


# 예제2
# self의 이해
class SelfTest:
    def function1():
        print("function1 called!")

    def function2(self):
        print(id(self))
        print("function2 called!")


self_test = SelfTest()
# self_test.function1()
SelfTest.function1()
self_test.function2()

print(id(self_test))
SelfTest.function2(self_test)


# 예제3
# 클래스 변수, 인스턴스 변수
class WareHouse:
    # 클래스 변수
    stock_num = 0

    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1

    def __del__(self):
        WareHouse.stock_num -= 1


user1 = WareHouse("kim")
user2 = WareHouse("Park")
user3 = WareHouse("Lee")

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__)  # 클래스 네임스페이스, 클래스 변수(공유)


print(user1.name)
print(user2.name)
print(user3.name)


print(user1.stock_num)
print(user2.stock_num)
print(user3.stock_num)


del user1
print(user2.stock_num)
print(user3.stock_num)
