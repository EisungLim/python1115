#전역변수
str = "Not Class Member"
#클래스 정의
class GString:
    def __init__(self):
        #인스턴스 맴버 변수
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #버그 발생~~
        print(self.str)

g = GString()
g.set("First Message")
g.print()
