# db1.py
from os import name
import sqlite3

#연결객체 리턴받기(임시로 메모리 작업)
# con = sqlite3.connect(":memory:")
# 영구적으로 파일에 남기기 
con = sqlite3.connect("test.db")

#실제 구문을 실행한 커서 객체
cur = con.cursor()
#테이블 구조(스키마) 생성
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
#1건을 입력 
cur.execute("insert into PhoneBook values ('derick','010-222');")
#입력 파라미터 처리(입력창을 통해서 받기)
name = "gildong"
phoneNumber = "010-111"
cur.execute("insert into PhoneBook values (?, ?);",(name,phoneNumber) )
#다중의 레코드 입력(2차원: 2행2열 데이터)
datalist = (("tom","010-123"), ("dsp","010-456"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)

#데이터 조회(Cursor클래스: Command + ResultSet)
cur.execute("select * from PhoneBook;")
# for row in cur:
#     print(row)
print("---fetchone()---")
print( cur.fetchone())
print("---fetchmany(2)---")
print( cur.fetchmany(2))
print("---fetchall()---")
cur.execute("select * from PhoneBook;")
print( cur.fetchall())

#지금상태는 전부 롤백(취소)


