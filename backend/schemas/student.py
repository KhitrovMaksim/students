import re

from pydantic import BaseModel, Field, EmailStr, validator, conlist


class Student(BaseModel):
    first_name: str = Field("Peter",
                            title="First name",
                            alias="First name",
                            description="First name [ minimum three characters ]",
                            max_length=100,
                            min_length=3,
                            strip_whitespace=True)
    last_name: str = Field("Berg",
                           title="Last name",
                           alias="Last name",
                           description="Last name [ minimum three characters ]",
                           max_length=100,
                           min_length=3,
                           strip_whitespace=True)
    date_of_birth: str = Field("01/01/2000",
                               title="Date of Birth",
                               alias="Date of Birth",
                               description="Date of Birth [ format 01/01/2000 ]",
                               max_length=10,
                               min_length=10)
    email: EmailStr = Field(title="Email",
                            alias="Email")
    phone: str = Field("(999) 999-9999",
                       title="Phone number",
                       alias="Phone number",
                       description="Phone number [ format (999) 999-9999 ]",
                       max_length=14,
                       min_length=14)
    favorite_sports: conlist(str, unique_items=True) = Field(["Golf", "Football", "Cricket", "Hockey", "Tennis"],
                                                             title="Favorite sports",
                                                             alias="Favorite sports",
                                                             description="Favorite sports [ checkbox ]")

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

    @validator('favorite_sports')
    def validate_favorite_sports(cls, v):
        if not all(item in ["Golf", "Football", "Cricket", "Hockey", "Tennis"] for item in v):
            raise ValueError("Please enter a valid phone number. An example: (999) 999-9999")
        return v

    class Config:
        anystr_strip_whitespace = True
