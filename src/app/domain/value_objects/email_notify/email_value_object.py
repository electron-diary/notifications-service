from typing import Self
from dataclasses import dataclass
import re

from app.domain.common.value_objects import DomainValueObject
from app.domain.common.exceptions import DomainValidationError


def email_validator(value: str) -> bool:
    pattern: str = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, value):
        return True
    else:
        return False


@dataclass(frozen=True)
class Email(DomainValueObject[str]):
    def validate(self: Self) -> None:
        if not self.to_raw():
            raise DomainValidationError(
                "Email cannot be empty"
            )
        if not isinstance(self.to_raw(), str):
            raise DomainValidationError(
                "Email must be a string"
            )

        if not email_validator(self.to_raw()):
            raise DomainValidationError(
                "Email must be a valid email"
            )