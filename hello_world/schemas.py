from pydantic import BaseModel


class IndexResponse(BaseModel):
    class Config:
        orm_mode = True

    hello_world: bool
    is_live: bool


class HelloWorldValues(BaseModel):
    class Config:
        orm_mode = True

    id: int
    value: str
