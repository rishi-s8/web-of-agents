from pydantic import BaseModel

class Handshake(BaseModel):
    title: str
    version: str
    description: str
