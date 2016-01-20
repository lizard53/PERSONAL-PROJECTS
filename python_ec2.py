import urllib
import pymysql
from boto.s3.connection import S3Connection
from boto.s3.key import Key
try:
	file = open('key.txt').read()
	login = file.split()
	conn=S3Connection(login[1],login[2])
	mybucket = conn.get_bucket('ec2dev')
	print "Connected to S3"

except:
	print "Unable to connect to S3"
	exit()

try:
	for j in mybucket.list():
		if j.name == 'login.txt':
			print j.name
			k = Key(mybucket)
			k.key = j.name
			k.open()
			file_1 = k.read()
			print "Successfully opened login.txt"
except:
	print "Unable to open File on S3"
	exit()

		
login = file_1.split()

try:
	conn = pymysql.connect(host=login[0],user= login[1],password=login[2],db= login[4])
	print "Connected successfully to RDS"
except:
	print "Unable to connect to RDS"
	exit()
cur = conn.cursor()
sql = "select * from dept"
cur.execute(sql)
result = cur.fetchone()
print (result)
conn.close()






