import pymongo
import requests

# 9/02/2023 - Thursday
# Exercise: The data in this database has been pulled from https://swapi.dev/.
# As well as 'people', the API has data on starships. In Python, pull data on all available starships from the API.
# Your goal will be to create a new starship collection in mongodb.
# The "pilots" key contains URLs pointing to the characters who pilot the starship.
# Use these to replace 'pilots' with a list of ObjectIDs from our characters collection,
# then insert the starships into their own collection. Use functions at the very least!


def count_starships():  # Function to return the number of starships as an integer
    starships_dict = requests.get("https://swapi.dev/api/starships").json()
    no_of_starships = starships_dict["count"]
    return no_of_starships


def starships():  # Function to return all the starships as dictionary's in a list
    starships_list = []
    count = 0
    starships_no = count_starships()
    i = 1
    while count < starships_no:  # While loop runs until the number of starships inserted into the list equals the
        # number of starships from count_starships()

        url = "https://swapi.dev/api/starships/" + str(i)
        request = requests.get(url)

        if request.status_code == 200:
            json_data = requests.get(url).json()
            starships_list.append(json_data)

            count += 1
            i += 1
        else:
            i += 1

    return starships_list


def change_pilot_name():  # Function to replace the pilot urls with the pilot id via searching for the pilots name.
    starships_no = count_starships()
    starships_info = starships()

    client = pymongo.MongoClient()  # Connecting to MongoDB
    db = client["starwars"]

    for i in (range(starships_no)):  # First loop iterates through each starship in the list
        for j in range(len(starships_info[i]["pilots"])):  # Second loop iterates through the pilots in each starship

            url = starships_info[i]["pilots"][j]  # The original pilots url
            names_dict = requests.get(url).json()  # Get request to obtain the pilots name

            search = names_dict["name"]  # Name of the pilot, to be searched through the characters collection

            pilot_id = db.characters.find_one({'name': search}, {'_id': 1})  # Find and save the id of the pilot
            starships_info[i]["pilots"][j] = pilot_id  # Replace replace pilot url with pilot_id

    return starships_info


def insert_into_mongodb():  # Function to insert the starships info into MongoDB as a collection of documents
    starships_data = change_pilot_name()
    client = pymongo.MongoClient()
    db = client["starwars"]
    col = db["starships"]
    col.insert_many(starships_data)


insert_into_mongodb()
