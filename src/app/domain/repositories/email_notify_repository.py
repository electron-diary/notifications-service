from typing import Self, Protocol
from abc import abstractmethod

from app.domain.entities.email_notify_entity import EmailNotificationEntity


class EmailNotificationRepository(Protocol):
    @abstractmethod
    async def send_email(self: Self, email_notification: EmailNotificationEntity) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )