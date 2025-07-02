from pydantic import BaseModel

class PersonResponse(BaseModel):
    id: int
    name: str
    age: int
    email: str

    model_config = {
        "from_attributes": True
    }
