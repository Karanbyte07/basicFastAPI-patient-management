from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pincode:int

class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address:Address

address_dict = {"city" : "Noida", "state" : "UP", "pincode": 201305 }
address1 = Address(**address_dict)

patient_dict = {"name" : "karan", "gender" : "male", "age" : 21, "address" : address1}
patient1 = Patient(**patient_dict)


print(patient1.name)
print(patient1.address)

