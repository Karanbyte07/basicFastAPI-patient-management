from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50,
                               title="enter the name of patient",
                               description="Give name under the 50chars",
                               examples=["nitish", "amit"])]
    age:int
    weight:float = Field(gt=0)
    married:bool
    email:EmailStr #for data validation use emailstr
    yt_video:AnyUrl #any kind of link validation
    allergies:Optional[List[str]]
    contact_details:Dict[str, str]

def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.email)
    print(patient.yt_video)
    print("Inserted in DB")

patient_info = {"name": "karan", "age":"21", "weight":66.4, "married": False, 
               "allergies": ["polen", 'dust'], 
               "email" : "abc@gmail.com",
               "yt_video" : "https://www.youtube.com/watch?v=lRArylZCeOs&t=1714s",
               "contact_details" : {"number" : "+91 123456780"}}

pateint1 = Patient(**patient_info)

insert_patient(pateint1)


