from pymongo import MongoClient 
  
try: 
    conn = MongoClient() 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 
  
# database name: mydatabase 
db = conn.users
  
# Created or Switched to collection names: myTable 
collection = db.accounts
  
# To find() all the entries inside collection name 'myTable' 
cursor = collection.find() 
for record in cursor: 
    print(record) 