# DemoRE.py
# 정규표현식:특정이 규칙이 있는 것 
import re

print( dir(re) )

result = re.match("[0-9]*th", "35th")
#매칭 오브젝트
print( result )
print( result.group() )

#match와 search함수의 차이 
print( bool(re.match("[0-9]*th", "  35th")) )
print( bool(re.search("[0-9]*th", "  35th")) )

#년도 찾기
print( bool(re.search("\d{4}", "올해는 2021년입니다.")) )
result = re.search("\d{4}", "올해는 2021년입니다.")
print( result.group() )

