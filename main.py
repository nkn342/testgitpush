import pymongo
client = pymongo.MongoClient("mongodb+srv://nikhil:nkn110011@nikhil.unpmd.mongodb.net/?retryWrites=true&w=majority")
db = client.test

d = {
    "name":"nikhil" ,
    "surname" :"kumar",
    "mailid" :"nikhilkumar3220@gmail.com"
}
db1 = client['main']
coll = db1['test']
coll.insert_one(d)