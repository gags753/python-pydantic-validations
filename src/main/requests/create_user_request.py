from pydantic import BaseModel, EmailStr
from datetime import date

class CreateUserRequest(BaseModel):
  name: str
  birth_date: date
  experience_in_years: int
  email: EmailStr