from datetime import datetime, timezone
from typing import Any, Dict

from pydantic import (
    BaseModel,
    ConfigDict,
    ValidationInfo,
    field_validator,
    root_validator,
)
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

    @root_validator(pre=True)
    def convert_input_datetime_add_tzinfo(
        cls: Any,
        values: Dict[str, Any],
    ) -> Dict[str, Any]:
        if isinstance(values, dict):
            for field_name, value in values.items():
                if isinstance(value, datetime) and values[field_name].tzinfo is None:
                    values[field_name] = values[field_name].replace(tzinfo=timezone.utc)

        return values

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
