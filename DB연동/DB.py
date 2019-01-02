import pymysql

conn = pymysql.connect(host="localhost" , user ="root" , password = "" , db = "test", charset="utf8")  #db연동
curs = conn.cursor()  # cursor생성
sql = "select * from member"  #sql문
curs.execute(sql)  #sql문 실행
alldata = curs.fetchall()  #data fetch
for i in range(0, len(alldata)) :
    print(alldata[i][5])

conn.close()


