from fastapi import APIRouter
from utils.models import Group, GroupName
from db.client import groups_data

router = APIRouter(
    prefix="/groups",
    tags=["groups"],
    responses={404: {"description": "Not found"}},
)


# group registration


@router.post("/register")
async def register_group(group: Group):
    try:
        groups_data.insert_one({
            "name": group.name,
            "id": group.id,
            "student1": {
                "name": group.student1.name,
                "id": group.student1.id
            },
            "student2": {
                "name": group.student2.name,
                "id": group.student2.id
            },
            "student3": {
                "name": group.student3.name,
                "id": group.student3.id
            },
        })
        return "Group registration successful!"
    except:
        return "Error has occured!"


# all groups data fetching


@router.get("/details")
def details():
    all_groups = list(groups_data.find({}, {'_id': 0}))
    return all_groups


# group data fetching with id


@router.get("/details/{group_id}")
def group_details(group_id: int):
    try:
        data = groups_data.find_one({"id": group_id}, {'_id': 0})
        if (data != None):
            return data
        else:
            raise Exception()
    except:
        return f"Group with id: {group_id} wasn't registered!"

# group members data fetching


@router.get("/members/{group_id}")
def group_members_by_id(group_id: int):
    data = groups_data.find_one({"id": group_id}, {'_id': 0})
    student_data = {
        "student1": {"name": data["student1"]["name"], "id": data["student1"]["id"]},
        "student2": {"name": data["student2"]["name"], "id": data["student2"]["id"]},
        "student3": {"name": data["student3"]["name"], "id": data["student3"]["id"]}
    }
    return student_data


# update group name

@router.post("/update_name")
def update_group_name(group: GroupName):
    query = {"id": group.id}
    new_values = {"$set": {"name": group.name}}
    try:
        old_data = groups_data.find_one(
            {"id": group.id}, {'_id': 0})
        groups_data.update_one(query, new_values)
        new_data = groups_data.find_one(
            {"id": group.id}, {'_id': 0})

        return {"old_data": old_data, "updated_data": new_data}
    except:
        return "Something went wrong!"
