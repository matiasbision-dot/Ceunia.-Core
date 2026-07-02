from fastapi import FastAPI
from ceunia.core import CEUNIA

app = FastAPI()
system = CEUNIA()

@app.post("/run")
def run(input_text: str):
    result = system.run(len(input_text))
    return {"output": result}
