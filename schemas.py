from pydantic import BaseModel,Field,ConfigDict

class PostBase(BaseModel):
    title:str=Field(min_length=2,max_length=20)
    content:str=Field(min_length=1,max_length=150)
    author:str=Field(min_length=1,max_length=20)

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    model_config=ConfigDict(from_attributes=True)
    id: int
    post_date:str