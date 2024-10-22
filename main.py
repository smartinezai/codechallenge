from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd


class PredictionRequest(BaseModel):
    Geschlecht: str
    Alter: int
    Fahrerlaubnis: bool 
    Regional_Code: int
    Vorversicherung: bool
    Alter_Fzg: str
    Vorschaden: bool
    Jahresbeitrag: float
    Vertriebskanal: int
    Kundentreue: int

app = FastAPI()


@app.post("/items/")
async def create_item(item: PredictionRequest):
    df = pd.DataFrame(columns=['Geschlecht', 'Alter', 'Fahrerlaubnis', 'Regional_Code', 'Vorversicherung', 'Alter_Fzg', 'Vorschaden', 'Jahresbeitrag','Vertriebskanal', 'Kundentreue'])
    df['Geschlecht'] = item.Geschlecht
    df['Alter'] = item.Alter
    df['Fahrerlaubnis'] = item.Fahrerlaubnis
    df['Regional_Code'] = item.Regional_Code
    df['Vorversicherung'] = item.Vorversicherung
    df['Alter_Fzg'] = item.Alter_Fzg
    df['Vorschaden'] = item.Vorschaden
    df['Jahresbeitrag'] = item.Jahresbeitrag
    df['Vertriebskanal'] = item.Vertriebskanal
    df['Kundentreue'] = item.Kundentreue
    categorical_cols =['Geschlecht', 'Alter_Fzg', "Vorschaden"]
    return item