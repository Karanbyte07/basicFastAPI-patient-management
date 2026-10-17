from pydantic import BaseModel,EmailStr, AnyUrl, computed_field
from typing import List, Dict, Optional

class Patient(BaseModel):
    name:str
    age:int
    height:float #mtr
    weight:float  #kgs
    married:bool
    email:EmailStr
    yt_video:AnyUrl
    allergies:Optional[List[str]]
    contact_details:Dict[str, str]

    #calculate the bmi with the given height and weight and bmi is dynamiacally created so the bmi is called the computed field
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round((self.weight/ self.height **2),2)
        return bmi


def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.email)
    print(patient.yt_video)
    print('BMI -> ' , patient.bmi)
    print("Inserted in DB")

patient_info = {"name": "karan", "age":"87", "weight":66.4, "height":5.7 ,"married": False,
               "allergies": ["polen", 'dust'],
               "email" : "abc@gmail.com",
               "yt_video" : "https://www.youtube.com/watch?v=lRArylZCeOs&t=1714s",
               "contact_details" : {"number" : "+91 123456780", "emergency" : "8792949"}}

pateint1 = Patient(**patient_info)

insert_patient(pateint1)
