import pymongo

client = pymongo.MongoClient()
db = client["starwars"]



# average height for female characters
# get female heights
# group everything together
# $avg to find average


# removing unknown heights and masses
# db.characters.update_many({"height":"unknown"},{"$unset":{"height":""}})
# db.characters.update_many({"height":"unknown"},{"$unset":{"mass":""}})
#
# # # Set height strings into integers
# db.characters.update_many({},[{"$set":{"height":{"$toInt":"$height"}}}])
#
# # sort out the comma problem
# db.characters.update_one({"mass":"1,358"},{"$set":{"mass":"1358"}})
#
# db.characters.update_many({},[{"$set": {"mass":{"$toDouble":"1358"}}}])
#
# characters = db.characters.find({}, {"height": 1, "mass": 1, "_id": 0})
# for person in characters:
#     print(person)

avg_f_height = db.characters.aggregate([{"$match": {"gender": "female"}}, {"$group":{"_id":"$gender", "avg_height":{"$avg": "$height"}}}])

for person in avg_f_height:
    print(person)