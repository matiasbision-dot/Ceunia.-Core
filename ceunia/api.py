
from fastapi import FastAPI
from ceunia.core import CEUNIA

app = FastAPI()
system = CEUNIA()

@app.post("/run")
def run(input_text: str):
    x = len(input_text)
    result = system.run(x)
    return {"input": input_text, "output": result}
