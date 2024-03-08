from typing import Any

from pydantic import BaseModel, ConfigDict, ValidationInfo, field_validator
from pydantic_core import PydanticUndefined


def hyphenize(field: str) -> str:
    return field.replace("_", "-")


class BaseEntity(BaseModel):
    model_config = ConfigDict(
        alias_generator=hyphenize,
        populate_by_name=True,
        arbitrary_types_allowed=True,
        validate_assignment=True,
        from_attributes=True,
    )

    @field_validator("*", mode="before")
    @classmethod
    def use_default_value(cls, value: Any, info: ValidationInfo) -> Any:
        if info.field_name and (
            cls.model_fields[info.field_name].get_default() is not PydanticUndefined
            and not cls.model_fields[info.field_name].is_required()
            and value is None
        ):
            return cls.model_fields[info.field_name].get_default()

        return value
