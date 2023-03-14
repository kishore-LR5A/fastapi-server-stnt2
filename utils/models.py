from pydantic import BaseModel


class Student(BaseModel):
    name: str
    id: int


class Group(BaseModel):
    name: str
    id: int
    student1: Student
    student2: Student
    student3: Student


class Project(BaseModel):
    group_id: int
    name: str
    desc: str


class GroupName(BaseModel):
    name: str
    id: int
