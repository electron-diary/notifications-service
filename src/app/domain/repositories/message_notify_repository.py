from typing import Self, Protocol
from abc import abstractmethod

from app.domain.entities.message_notify_entity import MessageNotificationEntity


class MessageNotificationRepository(Protocol):
    @abstractmethod
    async def send_message(self: Self, message_notification: MessageNotificationEntity) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )