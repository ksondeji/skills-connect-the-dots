import hashlib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Text(BaseModel):
    text: str

@app.post("/checksum")
def checksum_text(payload: Text):
    """Return a checksum of the submitted text."""
    checksum = hashlib.sha256(payload.text.encode("utf-8")).hexdigest()
    return {"checksum": checksum}
