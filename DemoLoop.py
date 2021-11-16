# DemoLoop.py

lst = [1,2,3,4,5,6,7,8,9,10]
for item in lst:
    if item > 5:
        break
    print("Item:{0}".format(item))

print("---continue구문---")
for item in lst:
    if item % 2 == 0:
        continue
    print("Item:{0}".format(item))
    
#수열함수 
print( list(range(10)) )
print( list(range(1,11)) )
print( list(range(2000, 2022)) )

#리스트 컴프리헨선 
lst = list(range(1,11))
result = [i**2 for i in lst if i > 5]
print(result)
d = {100:"apple",200:"kiwi",300:"orange"}
result = [v.upper() for v in d.values()]
print( result )

#필터링하는 함수 
#이름 규칙: 변수명, 함수명, 메서드명은 카멜 표기법(첫단어는 소문자로)
#클래스명: 파스칼 표기법(각 단어의 첫글자는 대문자로 표기) DemoCustomer, CompanyProduct 
print("---필터링 함수---")
def getBiggerThan20(i):
    return i > 20

lst = [10, 25, 30]
iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)

print("---람다 함수 사용---")
iterL = filter(lambda x:x>20, lst)
for item in iterL:
    print(item)

print("---맵함수---")
#스칼리(단일값) 리스트 
lst = [1,2,3,4,5]
for item in map(lambda x:x+10, lst):
    print(item)

