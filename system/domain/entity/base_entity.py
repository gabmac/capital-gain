from datetime import datetime, timezone
from typing import Any, Dict

from pydantic import BaseModel, root_validator


class BaseEntity(BaseModel):
    class Config:
        populate_by_name = True
        use_enum_values = True
        arbitrary_types_allowed = True
        validate_assignment = True
        from_attributes = True

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
