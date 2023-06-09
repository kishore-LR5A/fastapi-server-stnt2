from fastapi import FastAPI
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from routers import groups, projects

# mongo client
client = MongoClient(
    "mongodb+srv://yaadava_kishore:dMULvlVpDlLfT5Nc@stnt.qfx8k6g.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))

# current database will be stnt2
db = client["stnt2"]

# groups_data collection
groups_data = db["groups_data"]
projects_data = db["projects_data"]

app = FastAPI()


# home route
@app.get("/", tags=["home"])
def read_root():
    return {"project": "FastAPI server", "group-name": "Rx100", "group-id": 14}


app.include_router(groups.router)
app.include_router(projects.router)
