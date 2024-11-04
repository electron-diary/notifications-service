from typing import Self
from dataclasses import dataclass

from app.domain.common.value_objects import DomainValueObject
from app.domain.common.exceptions import DomainValidationError

@dataclass(frozen=True)
class PhoneNumber(DomainValueObject[int]):
    def validate(self: Self) -> None:
        if not self.to_raw():
            raise DomainValidationError(
                "Phone number cannot be empty"
            )
        if not isinstance(self.to_raw(), int):
            raise DomainValidationError(
                "Phone number must be an integer"
            )

        if len(self.to_raw()) <= 2 or len(self.to_raw()) > 24:
            raise DomainValidationError(
                "Phone number must be between 3 and 24 characters"
            )