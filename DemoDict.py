# DemoDict.py

tp = ("apple", "kiwi")
print( type (tp))
print( len (tp))

# 함수를 정의 
def times(a,b):
    return a+b, a*b

# 함수를 호출 
print( times(3,4) )

args = (5, 6)
times(*args)

print("id: %s, name: %s"% ("kim","김유신"))

#형식 변환
a = set((1,2,3))
print( type(a))
b = list(a)
print( b )
b.append(4)
print( b )

# 딕셔너리(사전식 구조)
colors = {"apple":"red","kiwi":"green"}
print( len(colors))
#검색
print( colors["apple"])
#입력
colors["banana"] = "yellow"
#삭제
del colors["apple"]
print(colors)

#장비를 관리한다.
device = {"아이폰":5, "아이패드":10, "윈도우타블렛":20}
#중지점(Break Point) 중단점
print(len(device))
print(device["아이폰"])
#입력
device["맥북"] = 15
#수정 
device["아이폰"] = 6
#삭제 
del device["아이패드"]
print(device)

#전화번호 
phone = {"kim":"1111","park":"2222"}
for item in phone.items():
    print(item)

for k,v in phone.items():
    print(k,v)

print( "kim" in phone)

print( "moon" not in phone)

for key in phone.keys():
    print(key)

for value in phone.values():
    print(value)