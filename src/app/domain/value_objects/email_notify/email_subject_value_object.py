from typing import Self
from dataclasses import dataclass

from app.domain.common.value_objects import DomainValueObject
from app.domain.common.exceptions import DomainValidationError


@dataclass(frozen=True)
class EmailSubject(DomainValueObject[str]):
    def validate(self: Self) -> None:
        if not self.to_raw():
            raise DomainValidationError(
                "Email subject cannot be empty"
            )
        if not isinstance(self.to_raw(), str):
            raise DomainValidationError(
                "Email subject must be a string"
            )