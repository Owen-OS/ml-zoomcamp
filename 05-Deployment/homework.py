import pickle
from fastapi import FastAPI
import json
from pydantic import BaseModel


class customer(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float



app = FastAPI()

@app.post("/model")
async def get_model_result(c: customer):
    #sh-5.3$ uvicorn homework:app --host 0.0.0.0 --port 9696


    with open("pipeline_v2.bin", "rb") as f:
        dv, model = pickle.load(f)

    student_dict = json.loads(c.json())
    print(f"Student Dict: {student_dict}")
    print(f"Type: {type(student_dict)}")

    X = dv.transform(student_dict)
    y_pred = model.predict_proba(X)[0, 1]


    return {"Probability": y_pred}

    
@app.post("/question3_and_4")
async def get_question3(c: customer):
    with open("pipeline_v1.bin", "rb") as f:
        dv, model = pickle.load(f)
    
    return get_results(dv, model, c)


@app.post("/question6")
async def get_question6(c: customer):
    with open("pipeline_v2.bin", "rb") as f:
        dv, model = pickle.load(f)
    
    return get_results(dv, model, c)

def get_results(dv, model, c):

    customer_dict = json.loads(c.json())
    X = dv.transform(customer_dict)
    y_pred = model.predict_proba(X)[0, 1]


    return {"Churn Probability" : y_pred}