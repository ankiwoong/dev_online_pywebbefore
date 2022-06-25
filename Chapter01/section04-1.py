# 데이터 타입

from nis import match
from unittest import result


v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name": "Kim",
    "age": 25
}
v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {7, 8, 9}

print(type(v_tuple))
print(type(v_set))
print(type(v_float))

i1 = 39
i2 = 939
big_int1 = 123456789123456789012345678901234567890
big_int2 = 999999999999999999999999999999999999999
f1 = 1.234
f2 = 3.939
f3 = .5
f4 = 10.

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2)
print(f3 + i2)

result = f3 + f2
print(result, type(result))

a = 5.
b = 4
c = .4
d = 7.7

print(type(a), type(b))
result2 = a + b
print(result2)

# 형변환
# int, float, complex(복소수)

print(int(result2))
print(float(c))
print(complex(3))
print(int(True))
print(int(False))
print(int('3'))
print(complex(False))

y = 100
y += 100
print(y)

# 수치 연산 함수
print(abs(-7))
n, m = divmod(100, 8)
print(n, m)

import math

print(math.ceil(5.1))
print(math.floor(3.874))