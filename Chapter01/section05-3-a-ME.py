# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

if "가을" in q1:
    print(q1.get("가을"))
else:
    pass

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

if "사과" in q2.values():
    print("포함")
else:
    pass

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
var1 = int(input("값을 입력하세요 : "))

if var1 >= 81:
    print("A학점")
elif var1 >= 61:
    print("B학점")
elif var1 >= 41:
    print("C학점")
elif var1 >= 21:
    print("D학점")
else:
    print("E학점")


var2 = int(input("값을 입력하세요 : "))
if var2 >= 61 and var2 <= 80:
    print("B학점")
elif var2 >= 41 and var2 <= 60:
    print("C학점")
elif var2 >= 21 and var2 <= 40:
    print("D학점")
elif var2 >= 0 and var2 <= 20:
    print("E학점")
else:
    print("A학점")


# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
var3, var4, var5 = 12, 6, 18
if var3 > var4 and var3 > var5:
    print(var3)
elif var4 > var5:
    print(var4)
else:
    print(var5)


# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
var6 = str(input("주민등록번호를 입력하세요 : ")).split("-")[1]
if int(list(var6)[0]) == 1 or int(list(var6)[0]) == 3:
    print("남자")
elif int(list(var6)[0]) == 2 or int(list(var6)[0]) == 4:
    print("여자")
else:
    print("잘못 입력하셨습니다.")


# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]
var7 = []

for i in q3:
    if i != "정":
        var7.append(i)
    else:
        pass

print(var7)


# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
var8 = []

for i in range(101):
    if i % 2 == 1:
        var8.append(str(i))

print(" ".join(var8))

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
var9 = []

for i in q4:
    if len(i) >= 5:
        var9.append(i)

print(" ".join(var9))

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
var10 = []

for i in q5:
    if i.isupper() != True:
        var10.append(i)

print(" ".join(var10))

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
var11 = []
var12 = []

for i in q6:
    if i.isupper() == True:
        var11.append(i)
    else:
        var12.append(i)

print(" ".join(var11).lower())
print(" ".join(var12).upper())

"""

사과
포함
값을 입력하세요 : 20
E학점
값을 입력하세요 : 20
E학점
18
주민등록번호를 입력하세요 : 999999-122222
남자
['갑', '을', '병']
1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99
study python anaconda
b c e h
a d f g
B C E H

"""
