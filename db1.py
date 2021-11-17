# db1.py
import sqlite3

#연결객체 리턴받기(임시로 메모리 작업)
con = sqlite3.connect(":memory:")
#실제 구문을 실행한 커서 객체
cur = con.cursor()
#테이블 구조(스키마) 생성
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
#1건을 입력 
cur.execute("insert into PhoneBook values ('derick','010-222');")

#데이터 조회
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)
