# dbms_mysql_select.py


import pymysql

# MySQL 서버에 연결
conn = pymysql.connect(
    host="localhost",       # MySQL 서버 주소
    user="root",
    passwd="1234",
    database="exampledb",
)

# 커서 생성 => 명령어 작성 (데이터베이스 관련)
cursor = conn.cursor()

# 커서 통해 명령어 실행
sql = """
INSERT INTO employees(name,DeptID,ManagerID)
VALUES(108, 'lee', 8, 101);
"""



cursor.execute(sql)
conn.commit()

print("데이터 삽입 완료")

# MySQL 서버에 연결 헤제
conn.close()