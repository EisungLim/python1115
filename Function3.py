# Function3.py
#전역 변수
x = 1
def func(a):
    return a+x 

#호출 
print( func(1))

def func2(a):
    #지역 변수(LGB))
    x = 2
    return a + x

#호출 
print( func2(1))

#기본값 셋팅 
def times(a=10, b=20):
    return a*b

#호출 
print( times())
print( times(3))
print( times(3,4))

#키워드 인자 
def connectURI(server, port):
    strURL = "http://" + server + ":" + port
    return strURL

#호출 
print( connectURI("naver.com", "80"))
print( connectURI(port="80",server="naver.com"))

#가변인자(다양한 상황)
def union(*ar):
    result = [] 
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
            
    return result


#호출(중단점, Break Point) 
print( union ("HAM","EGG"))
print( union ("HAM","EGG","SPAM"))

#정의되지 않은 인자(필수 입력과 옵션 입력이 있는 경우)
def userURIBuilder(server, port, **user):
    strURL = "http://" + server + ":"  + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL

#호출 
print ( userURIBuilder ("naver.com", "80", id="kim", passwd="1234"))
print ( userURIBuilder ("naver.com", "80", id="kim", passwd="1234",
    name="mike"))