from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str= Field(max_length=50)
    age:int
    weight:float = Field(gt=0)
    married:bool
    email:EmailStr #for data validation use emailstr
    yt_video:AnyUrl #any kind of link validation
    allergies:Optional[List[str]]
    contact_details:Dict[str, str]

    #to check in the email there is icici.com or hdfc.com is present or not using field validator
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ["hdfc.com", "icici.com"]
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value

    #uppercase the name field
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()

    #modes - before and after (after type conversion give output in after mode )
    #default in after mode
    #before - it give same as the value have given in str then it can not compare with the int
    @field_validator('age', mode="after")
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError("Age should be in between 0 and 100")

def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.email)
    print(patient.yt_video)
    print("Inserted in DB")

patient_info = {"name": "karan", "age":"21", "weight":66.4, "married": False, 
               "allergies": ["polen", 'dust'], 
               "email" : "abc@hdfc.com",
               "yt_video" : "https://www.youtube.com/watch?v=lRArylZCeOs&t=1714s",
               "contact_details" : {"number" : "+91 123456780"}}

pateint1 = Patient(**patient_info)

insert_patient(pateint1)


