from pymongo import MongoClient
from pymongo.server_api import ServerApi

# mongo client
client = MongoClient(
    "mongodb+srv://yaadava_kishore:dMULvlVpDlLfT5Nc@stnt.qfx8k6g.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))

# current database will be stnt2
db = client["stnt2"]

# groups_data collection
groups_data = db["groups_data"]
projects_data = db["projects_data"]