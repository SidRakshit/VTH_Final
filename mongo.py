#install-> pip install pymongo
import pymongo
import datetime
myclient = pymongo.MongoClient("mongodb+srv://2303singhaditya:2uexx5LEIpgLN5kB@cluster0.h3vba0v.mongodb.net/")

csu = "timepass@gmail.com"
# mydb = myclient["mydatabase"]
print(myclient.stockSim.list_collection_names())

post = {
    "name": "Mike",
    "userid": "My first blog post!",
    "email": "hokie@gmail.com",
    "pwd": "hokiebird",
    "budget": 10000,
}
stockSim_db = myclient.stockSim
users_collection = stockSim_db.Users

# 3. Insert the post into the 'users' collection
insert_result = users_collection.insert_one(post)
print(f"Inserted document with ID: {insert_result.inserted_id}")

mike_document = users_collection.find_one({"name": "Mike"})

if mike_document:
    print(mike_document)
else:
    print("No document found with the name 'Mike'.")

for user in users_collection.find():
    print(user)