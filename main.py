from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from catboost import CatBoostClassifier
import uvicorn
import sys

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
model = CatBoostClassifier()
model.load_model("catmodel", format='cbm')

@app.post("/items/")
async def create_item(item: PredictionRequest):
    df = pd.DataFrame(columns=['Geschlecht', 'Alter', 'Fahrerlaubnis', 'Regional_Code', 'Vorversicherung', 'Alter_Fzg', 'Vorschaden', 'Jahresbeitrag','Vertriebskanal', 'Kundentreue'])
    df.loc[0] = [item.Geschlecht, item.Alter, item.Fahrerlaubnis, item.Regional_Code, item.Vorversicherung, item.Alter_Fzg, item.Vorschaden, item.Jahresbeitrag, item.Vertriebskanal, item.Kundentreue]
    print(df)
    
    pred = model.predict(df)
    print(pred)
    return { 'result': bool(pred[0]) }


def main():
  try:
    uvicorn.run(app, host="0.0.0.0", port = 80)

  except Exception as e:
    print(f'[-]  Major issue starting web server: {e}')
    print(e)
    return 1


if __name__ == "__main__":
    sys.exit(main())