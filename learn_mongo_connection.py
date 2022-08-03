import pymongo
import requests
import json
from bson import ObjectId
from enum import unique


# Machine hosting our database
cluster = pymongo.MongoClient("mongodb+srv://ycattaneo:yusuf33@cluster0.ridin.mongodb.net/?retryWrites=true&w=majority")
db = cluster.twitter
collection = db.original_tweets
# collection = db.reply_tweets

# Establishing a unique id
# collection.create_index({"id": 1}, { unique: True })



## Rename collection
# collection.rename("original_tweets")

## Creating a new collection
# replies = db["reply_tweets"]
#  Important: In MongoDB, a collection is not created until it gets content!
# post_values = {"_id": 0, "name": "Time", "score": 5}
# replies.insert_one(post_values)

# post_values = {"_id": 0, "name": "Time", "score": 5}
# post_values = { "name": "Yusuf", "score": 10}

# # Posting data (writing to a document)
# ## _id field will be auto incremented if not supplieda
# collection.insert_one(post_values)


# post_1 = {"_id": 1, "name": "Iby", "score": 7}
# post_2 = {"_id": 2, "name": "Maryam", "score": 8}
# ## Writing multiple values 
# collection.insert_many([post_1, post_2])

## Finding a value
# results = collection.find({"name": "Iby"})
# for result in results:
#     print(result["score"])

# single_result = collection.find_one({"id": 1550821177693769728})
# print(single_result)


# # Remove all values 
# remove_results = collection.delete_one({"id": 1550821177693769728})

# remove_results = collection.delete_one({"_id": ObjectId('62e981996974dd4ed793777d')})

# # All Results
# all_results = collection.find({})
# for x in all_results:
#     print(x)

# # Updating Fields
# update = collection.update_one({"_id": 1}, {"$set": {"name": "Alex"}})

# # Add a new field
# update = collection.update_one({"_id": 1}, {"$set": {"hello": 5}})

# # Increment Field (so hello should now be 10)
# update = collection.update_one({"_id": 1}, {"$inc": {"hello": 5}})

# # Get number of documents
# doc_count = collection.count_documents({"_id": 1})
# print(doc_count)
