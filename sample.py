# importing module 
from pymongo import MongoClient 
import urllib
# creation of MongoClient 
client=MongoClient() 
  
# Connect with the portnumber and host 
#client = MongoClient('mongodb://localhost:27017/')
  
"""username = urllib.parse.quote_plus('Sandeep1997')
password = urllib.parse.quote_plus('Sandeep1997')
#mongodb+srv://<username>:<password>@movies-8krg1.mongodb.net/test?retryWrites=true&w=majority
client = MongoClient("mongodb://%s:%s@movies-8krg1.mongodb.net/test?retryWrites=true&w=majority" % (username, password))
"""

client = MongoClient("mongodb+srv://Sandeep1997:Sandeep1997@movies-8krg1.mongodb.net/test?retryWrites=true&w=majority")


print(client.list_database_names())
"""mydatabase = client["sandeep"] 
  
# Access collection of the database 
#mycollection=mydatabase["accounts"] 
  
# dictionary to be added in the database 
rec={ 
"title": 'MongoDB and Python',  
"description": 'MongoDB is no SQL database',  
"tags": ['mongodb', 'database', 'NoSQL'],  
"viewers": 104 
}
rec = mydatabase.dummy.insert(rec)"""
