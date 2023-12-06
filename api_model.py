from pydantic import BaseModel, Field

# Let's create a class that validates the type of requested parameters
class UserPredDate(BaseModel):
    year: str = Field(...)
    month : str = Field(...)
  

