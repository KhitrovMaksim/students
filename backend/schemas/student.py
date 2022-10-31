import re

from pydantic import BaseModel, Field, EmailStr, validator
from typing import Optional


class Student(BaseModel):
    first_name: str = Field(title="First name",
                            description="First name [ minimum three characters ]",
                            max_length=100,
                            min_length=3,
                            strip_whitespace=True)
    last_name: str = Field(title="Last name",
                           description="Last name [ minimum three characters ]",
                           max_length=100,
                           min_length=3,
                           strip_whitespace=True)
    date_of_birth: str = Field(title="Date of Birth",
                               description="Date of Birth [ format 01/01/2000 ]",
                               max_length=10,
                               min_length=10)
    email: EmailStr = Field(title="Email")
    phone: str = Field(title="Phone number",
                       description="Phone number [ format (999) 999-9999 ]",
                       max_length=14,
                       min_length=14)
    favorite_sports: Optional[str] = Field(title="Favorite sports",
                                           description="Favorite sports [ checkbox ]",
                                           max_length=250)

    @validator('date_of_birth')
    def validate_date_of_birth(cls, v):
        regex = "^(0[1-9]|1[0-9]|2[0-9]|3[0-1])(/)(0[1-9]|1[0-2])(/)(1[9]|2[0])[0-9][0-9]$"
        if not re.match(regex, v):
            raise ValueError("Please enter a valid date of birth. An example: 01/01/2000")
        return v

    @validator('phone')
    def validate_phone_number(cls, v):
        regex = "^[(]([0-9]{3})[)][ ]([0-9]{3})(-)([0-9]{4})$"
        if not re.match(regex, v):
            raise ValueError("Please enter a valid phone number. An example: (999) 999-9999")
        return v

    class Config:
        anystr_strip_whitespace = True
