import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd="admin", db='ytms')
cur = conn.cursor()
cur.execute("select * from student")
for r in cur:
    print(r)
cur.close()
conn.close()