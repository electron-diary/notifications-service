from typing import Self
from dataclasses import dataclass

from app.domain.common.value_objects import DomainValueObject
from app.domain.common.exceptions import DomainValidationError


@dataclass(frozen=True)
class MessageContent(DomainValueObject[str]):
    def validate(self: Self) -> None:
        if not self.to_raw():
            raise DomainValidationError(
                "Message content cannot be empty"
            )
        if not isinstance(self.to_raw(), str):
            raise DomainValidationError(
                "Message content must be a string"
            )
        if len(self.to_raw()) > 100:
                raise DomainValidationError(
                    "Message content cannot be longer than 1000 characters"
                )