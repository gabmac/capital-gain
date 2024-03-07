from pydantic import BaseModel


class BaseDTO(BaseModel):
    class Config:
        populate_by_name = True
        use_enum_values = True
        arbitrary_types_allowed = True
        validate_assignment = True
        from_attributes = True
