from pydantic import Field

from system.application.dto.base_dto import BaseDTO


class OperationTaxDto(BaseDTO):
    tax: float = Field(description="Tax to pay given an operation")
