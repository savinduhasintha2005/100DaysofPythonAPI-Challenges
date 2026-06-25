from pydantic import BaseModel


class TextRequest(BaseModel):
    text:str

class TextResponse(BaseModel):
    orginal:str
    uppercase:str
    lowercase:str
    titlecase:str
    capitalize:str

