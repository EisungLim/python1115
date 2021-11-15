# Function2.py
#리턴을 하지 않는 함수
def setValue(newValue):
    x = newValue

#호출 
result = setValue(5)
print(result)

#Tuple을 리턴
def times(a,b):
    return a+b, a*b

#호출0
result = times(3,4)
print(result)

#참조를 전달(Pass By Reference)
def change(x):
    #내부의 복사본 생성(깊은 복사-Deep Copy)
    x1 = x[:]
    x[0] = "H"
    print("함수 내부:", x1)

#함수를 호출 
wordlist = ["J","A","M"]
change(wordlist)
print("함수 호출후:",wordlist)