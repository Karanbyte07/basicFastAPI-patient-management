import json
from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(..., description="ID of the Patient", examples=["P001"])]
    name: Annotated[str, Field(..., description="Name of the Patient")]
    city : Annotated[str, Field(..., description="City where the patient living")]
    age : Annotated[int, Field(..., gt = 0, lt = 100, description="age of the patient")]
    gender : Annotated[Literal['male', 'female', 'others'], Field(..., description="Gender of the patient")]
    height : Annotated[float, Field(...,gt = 0, description="height of the patient in mtrs")]
    weight : Annotated[float, Field(...,gt = 0,  description="weight of the patient in kgs")]

    #calculate bmi
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round((self.weight/self.height ** 2),2)
        return bmi

    #create verdict for the bmi 
    @computed_field
    @property
    def verdict(self) -> str:
        if self.weight < 18.5:
            return 'Underweight'
        elif self.weight < 25:
            return 'Normal'
        else:
            return 'Obese'

#load the data
def load_data():
    with open ("patients.json", "r") as f:
        data = json.load(f)
    return data

#save the data 
def save_data(data):
    with open('patients.json', "w") as f:
        json.dump(data, f)


@app.get("/")
def home():
    return {'message' : 'Patient managament system API'}


@app.get("/about")
def about():
    return {'message' : 'Learning fastAPI through this project'}


@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id : str = Path(..., description='ID of the patient', example='P001')):
    #load all the data
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient Not Found!")

@app.get('/sort')
def sort_patients(sort_by : str = Query(..., description='Sort on the basis of Height, Weight or BMI'),
                  order : str = Query('asc', description='Sort in asc or desc order')):
    valid_fields = ['height', 'weight', 'bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail='Invaild field select from {valid_fields}')
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select from asc or desc')

    data = load_data()
    sorted_data = sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=order == 'desc'
    )
    return sorted_data

#create a patient

@app.post("/create")
def create_patient(patient : Patient):
    #load existing data
    data = load_data()

    #check if the patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")
    #new patient add to the database
    data[patient.id] = patient.model_dump(exclude={'id'})

    #save the data
    save_data(data)

    return JSONResponse(status_code=201, content={"message" : "patient created successfully"})