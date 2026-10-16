import json
from fastapi import FastAPI, Path, HTTPException, Query

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

 