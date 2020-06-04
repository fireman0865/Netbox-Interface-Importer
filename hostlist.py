import psycopg2 as p
import hostnames
from hostnames import hostset
query=("""select id from dcim_device where name in {}""".format(hostset))

host=input("Enter hostname of your database")
db=input("Enter name of your database")
user=input("Enter username of your database")
pass=input("Enter password of your database")

conn=p.connect(host=host,database=db,user=user,password=pass)
cur=conn.cursor()
cur.execute(query)
rows=cur.fetchall()

listnames=[row for row in rows]
hostliste=[int(str(x).replace('(','').replace(',)','')) for x in listnames]
