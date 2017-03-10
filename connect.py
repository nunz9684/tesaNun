from pymongo import MongoClient 
client = MongoClient('localhost',27017)
client = MongoClient()
db = client.info
collect = db.info

print "===== Before insert ====="
datas = collect.find()
for data in datas :
	print data

collect.insert({"Humidity":"11","Picture":"mmmma"})
print "==== After insert ====="
datas = collect.find()
for data in datas :
	print data
print "xxxxxxxxxxx END xxxxxxxxxxxxxx"
