from fastapi import APIRouter
from utils.models import Project
from db.client import projects_data

router = APIRouter(
    prefix="/projects",
    tags=["projects"],
    responses={404: {"description": "Not found"}},
)


#  project regisration


@router.post("/register/")
def register_project(project: Project):
    try:
        projects_data.insert_one({
            "name": project.name,
            "id": project.group_id,
            "desc": project.desc
        })
        return "project registration successful!"
    except:
        return "Error has occured!"


# all project names


@router.get("/names")
def project_names():
    all_project_names = [x["name"]
                         for x in list(projects_data.find({}, {'_id': 0}))]
    return all_project_names

# all groups data fetching


@router.get("/details")
def project_details():
    all_projects = list(projects_data.find({}, {'_id': 0}))
    return all_projects


# projects data fetching with id


@router.get("/details/{group_id}")
def project_details_by_id(group_id: int):
    try:
        data = projects_data.find_one({"id": group_id}, {'_id': 0})
        if (data != None):
            return data
        else:
            raise Exception()
    except:
        return f"Project with group id: {group_id} wasn't registered!"


# update project data

@router.post("/update")
def update_project(project: Project):
    query = {"group_id": project.group_id}
    new_values = {"$set": {"name": project.name, "desc": project.desc}}
    try:
        old_data = projects_data.find_one(
            {"group_id": project.group_id}, {'_id': 0})

        projects_data.update_one(query, new_values)
        new_data = projects_data.find_one(
            {"group_id": project.group_id}, {'_id': 0})
        return {"old_data": old_data, "updated_data": new_data}
    except:
        return "Something went wrong!"
