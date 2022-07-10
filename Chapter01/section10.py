# Section 10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임)프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일, 문법 체크

# SyntaxError : 잘못된 문법
# SyntaxError: EOL while scanning string literal
# SyntaxError: invalid syntax

# print('Test)
# if True
#     pass
# x => y

# NameError : 참조변수 없음
# NameError: name 'c' is not defined
a = 10
b = 15
# print(c)

# ZeroDivisionError : 0 나누기 에러
# ZeroDivisionError: division by zero
# print(10 / 0)

# IndexError : 인덱스 범위 오버
# IndexError: list index out of range
x = [10, 20, 30]
# print(x[3])

# KeyError : 주로 딕셔너리에서 발생
# KeyError: 'hobby'
dic = {"name": "Kim", "Age": 33, "City": "Seoul"}
# print(dic["hobby"])

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외
# AttributeError: module 'time' has no attribute 'month'
import time

# print(time.month())

# ValueError : 참조 값이 없을 때 발생
# ValueError: list.remove(x): x not in list
# ValueError: 10 is not in list
x = [1, 5, 9]
# x.remove(10)
# x.index(10)

# FileNotFoundError : 외부 파일 처리 오류
# FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'
# f = open("test.txt", "r")

# TypeError
# TypeError: can only concatenate list (not "tuple") to list
# TypeError: can only concatenate list (not "str") to list
x = [1, 2]
y = (1, 2)
z = "test"

# print(x + y)
# print(x + z)

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생시 예외 처리 코딩 권장(EAFP 코딩 스타일)

# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명 1
# except : 에러명 2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

# 예제1
name = ["Kim", "Lee", "Park"]

try:
    z = "Kim"
    x = name.index(z)
    print("{} Found it! in name".format(z, x + 1))
except ValueError:
    print("Not found it! = Occurred ValueError!")
else:
    print("Ok! else!")


# 예제2
try:
    z = "Jin"
    x = name.index(z)
    print("{} Found it! in name".format(z, x + 1))
except:
    print("Not found it! = Occurred ValueError!")
else:
    print("Ok! else!")

# 예제3
try:
    z = "Kim"
    x = name.index(z)
    print("{} Found it! in name".format(z, x + 1))
except ValueError:
    print("Not found it! = Occurred ValueError!")
else:
    print("Ok! else!")
finally:
    print("finally ok!")

# 예제4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴
try:
    print("Try")
finally:
    print("Ok Finaly")


# 예제5
try:
    z = "Kim"
    x = name.index(z)
    print("{} Found it! in name".format(z, x + 1))
except ValueError as l:
    print(l)
except IndexError:
    print("Not found it! = Occurred ValueError!")
except Exception:
    print("Not found it! = Occurred ValueError!")
else:
    print("Ok! else!")
finally:
    print("finally ok!")

# 예제6
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = "Kim"
    if a == "Kim":
        print("OK 허가!")
    else:
        raise ValueError
except ValueError:
    print("문제 발생!")
except Exception as e:
    print(e)
else:
    print("OK!")
