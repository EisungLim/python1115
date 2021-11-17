# DemoStr.py

# print( dir(str) )

strA = "python is very powerful"
print( len(strA))
print( strA.capitalize())
print( strA.count("p"))
print( strA.count("p",7))

print("demo.ppt".endswith("ppt"))
print("MBC2580".isalnum())
print("MBC2580".isdecimal())
print("2580".isdecimal())

#앞뒤에 공백문자 제거
strB = "<<<  spam and ham  >>>"
print( strB )
result = ( strB.strip("<> "))
print( result )

#치환하는 경우 
result = result.replace("spam", "spam egg")
print( result )
lst = result.split()
print( lst )
print("---하나의 문자열로 합치기---")
print( ":)".join(lst))







