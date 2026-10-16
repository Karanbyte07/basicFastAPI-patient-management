import json
from fastapi import FastAPI, Path, HTTPException

app = FastAPI()

def load_data():
    with open ("patients.json", "r") as f:
        data = json.load(f)
    return data


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

 