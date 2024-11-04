from typing import Self
from dataclasses import dataclass

from app.domain.common.value_objects import DomainValueObject
from app.domain.common.exceptions import DomainValidationError


@dataclass(frozen=True)
class EmailContent(DomainValueObject[str]):
    def validate(self: Self) -> None:
        if not self.to_raw():
            raise DomainValidationError(
                "Email content cannot be empty"
            )
        if not isinstance(self.to_raw(), str):
            raise DomainValidationError(
                "Email content must be a string"
            )