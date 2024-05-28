from pydantic import BaseModel

class BlogModel(BaseModel):
    title : str
    sub_title : str
    content : str
    athor : str
    tags : list

class UpdateBlogModel(BaseModel):
    title : str = None
    sub_title : str = None
    content : str = None
    athor : str = None
    tags : list = None

