from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel


app = FastAPI()



students = {
    1:{
        "name":"imran",
        "age":14,
        "study_class":9
    },

    2:{
        "name":"sheikh",
        "age":20,
        "study_class":8
    },

    3:{
        "name":"neheru",
        "age":10,
        "study_class":4
    }

}

class Student(BaseModel):
    name: str
    age: int
    study_class: int

class UpdateStudent(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    study_class : Optional[int] = None

@app.get("/")
def index():
    for i in students:
        return students
    return {"name":"Imran Rahman 890"}



@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path (description="The student id goes here")):
    return students[student_id]


@app.get("/get-by-name")
def get_student(age : int,name: Optional[str] = None): # If we want to make the name not always required
    for student_id in students:                         # as the name is optional. python doesn't allow optional                                                  # parameters before the required parameters 
        if students[student_id]['name']==name:          # a * on the beginning will also work
            return students[student_id]
    return {"Data":"Not Found"}



@app.post("/create-student/{student_id}")

def create_student(student_id: int, student:Student):
    if student_id in students:
        return {"ERROR":"Student Exists"}
    students[student_id] = student

    return students[student_id]


@app.put("/update-student/{student_id}")

def update_student(student_id : int, student: UpdateStudent):

    if student_id not in students:
        return {"ERROR":"Student not found"}
    
    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.study_class != None:
        students[student_id].study_class = student.study_class

    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id : int):

    if student_id not in students:
        return {"ERROR":"The student does not exist"}
    
    del students[student_id]

    return {"Message":"Deleted"}