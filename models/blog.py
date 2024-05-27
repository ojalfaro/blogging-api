from pydantic import BaseModel

class BlogModel(BaseModel):
    title : str
    sub_title : str
    content : str
    athor : str
    tags : list