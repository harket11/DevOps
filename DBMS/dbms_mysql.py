# dbms_mysql.py


import pymysql

# MySQL 서버에 연결
conn = pymysql.connect(
    host="localhost",       # MySQL 서버 주소
    user="root",
    passwd="1234",
    database="exampledb",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)

# 커서 생성 => 명령어 작성 (데이터베이스 관련)
cursor = conn.cursor()

# 커서 통해 명령어 실행
cursor.execute("SELECT DATABASE()")

# 한번 호출에 하나의 Row를 가져올 때 사용
print("현재 데이터베이스 : ", cursor.fetchone())
# print("현재 데이터베이스 : ", cursor.fetchall())
# print("현재 데이터베이스 : ", cursor.fetchmany(2))

# MySQL 서버에 연결 헤제
conn.close()