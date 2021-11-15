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
    
result = times(3,4)
print(result)