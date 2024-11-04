from typing import Self
from dataclasses import dataclass
from datetime import datetime

from app.domain.common.value_objects import DomainValueObject
from app.domain.common.exceptions import DomainValidationError


@dataclass(frozen=True)
class MessageSendedAt(DomainValueObject[datetime]):
    def validate(self: Self) -> None:
        if not self.to_raw():
            raise DomainValidationError(
                "Message date at cannot be empty"
            )
        if not isinstance(self.to_raw(), datetime):
            raise DomainValidationError(
                "Message date must be a datetime"
            )