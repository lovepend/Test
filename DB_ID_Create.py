import sqlite3

# SQLite 연결 객체 생성
con = sqlite3.connect('ID.db') 

# 커서 객체 생성
cursor = con.cursor()


# ####################### 테이블 생성#########################

# # 테이블 생성 SQL 문
# create_sql = '''
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     Sid TEXT NOT NULL,
#     Spw TEXT NOT NULL
# );
# '''

# # 테이블 생성
# cursor.execute(create_sql)

# # # 변경사항 저장
# # con.commit()

# # 데이터 삽입 SQL 문
# insert_sql = "INSERT INTO users (name, Sid, Spw) VALUES (?, ?, ?);"

# # 다중의 행을 삽입
# userlist = (("1","pend","*Zoavld4fkd"), 
#             ("2","lovepend2","*Zoavld4fkd"),
#             ("3","lovepend3","*Zoavld4fkd"),
#             ("4","parkmc7","*Zoavld4fkd"),
#             ("5","jhrep1201","1902217**"),
#             )
# cursor.executemany(insert_sql, userlist)

# ##################################################

# 데이터 조회 SQL 
select_sql = "SELECT * FROM users ;"
# 데이터 조회
cursor.execute(select_sql)

# 결과 가져오기
rows = cursor.fetchall()

# 결과 출력
for row in rows:
    print(row)

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print(*rows, sep="\n")