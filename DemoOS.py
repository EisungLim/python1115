# DemoOS.py
import random

print( random.random() )
print( random.random() )
print( [random.randrange(20) for i in range(10)] )
print( random.sample(range(20),5) )

#파일이름 다루기 
from os.path import * 

print( abspath("python.exe") )
print( basename("c:\\work\\python.exe") )
print( getsize("c:\\python38\\python.exe") )


#운영체제 정보
import os
print("운영체제이름:", os.name)
# os.system("notepad.exe")

#파일 리스트, 폴더 리스트 
import glob
print( glob.glob("c:\\work\\*.py"))

os.chdir("..")
print("현재 작업 폴더:", os.getcwd())
os.chdir("c:\\work")
for item in glob.glob("*.*"):
    print(item)


