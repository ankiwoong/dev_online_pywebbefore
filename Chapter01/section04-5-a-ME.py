# Section04-5
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형
# 데이터 타입 관련 퀴즈(정답은 영상)

# 1. 아래 문자열의 길이를 구해보세요.
from posixpath import split


q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print(len(q1))

# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon
print("\tapple;orange;banana;lemon")

# 3. 화면에 * 기호 100개를 표시하세요.
print("*" * 100)

# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.
var1 = "30"
print(type(var1))
print(int(var1), type(int(var1)))
print(float(var1), type(float(var1)))
print(complex(var1), type(complex(var1)))
print(str(var1), type(str(var1)))

# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.
var2 = "Niceman"
print(var2[4:])
print(var2[4 : len(var2)])

# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"
var3 = "Strawberry"
print(var3[::-1])
var4 = list(var3)
var4.reverse()
print("".join(var4))

# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"
var5 = "010-7777-9999"
var6 = var5.split("-")
print("".join(var6))

# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"
var7 = "http://daum.net"
print(var7[7:])

# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"
var8 = "NiceMan"
print(var8.upper())
print(var8.lower())

# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"
var9 = "abcdefghijklmn"
print(var9[2:5])

# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
var10 = ["Banana", "Apple", "Orange"]
del var10[1]
print(var10)
var11 = ["Banana", "Apple", "Orange"]
var11.remove("Apple")
print(var11)

# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)
var12 = (1, 2, 3, 4)
print(list(var12), type(list(var12)))

# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>
var13 = {"성인": 100000, "청소년": 70000, "아동": 30000}
print(var13, type(var13))

# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
var13["소아"] = 0
print(var13)

# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.
print(var13.keys())

# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.
print(var13.values())

"""

38
        apple;orange;banana;lemon
****************************************************************************************************
<class 'str'>
30 <class 'int'>
30.0 <class 'float'>
(30+0j) <class 'complex'>
30 <class 'str'>
man
man
yrrebwartS
yrrebwartS
01077779999
daum.net
NICEMAN
niceman
cde
['Banana', 'Orange']
['Banana', 'Orange']
[1, 2, 3, 4] <class 'list'>
{'성인': 100000, '청소년': 70000, '아동': 30000} <class 'dict'>
{'성인': 100000, '청소년': 70000, '아동': 30000, '소아': 0}
dict_keys(['성인', '청소년', '아동', '소아'])
dict_values([100000, 70000, 30000, 0])

"""

# *** 결과 값만 정확하게 출력되면 됩니다. ^^* 고생하셨습니다. ***
