from typing import Self
from datetime import datetime

from app.domain.entities.message_notify_entity import MessageNotificationEntity
from app.domain.repositories.message_notify_repository import MessageNotificationRepository
from app.domain.value_objects.message_notify.message_content_value_object import MessageContent
from app.domain.value_objects.message_notify.message_sended_at_value_object import MessageSendedAt
from app.domain.value_objects.message_notify.phone_number_value_object import PhoneNumber
from app.application.interfaces.interactor import Interactor
from app.application.dto.send_message_notification_request_dto import SendMessageNotificationRequestDto


class SendEmailNotificationUseCase(Interactor[SendMessageNotificationRequestDto, None]):
    def __init__(self: Self, message_notifications_repository: MessageNotificationRepository) -> None:
        self.message_notification_repository: MessageNotificationRepository = message_notifications_repository

    async def __call__(self: Self, request: SendMessageNotificationRequestDto) -> None:
        time_now: datetime = datetime.now()
        notification_entity: MessageNotificationEntity = MessageNotificationEntity(
            contact=PhoneNumber(request.phone_number),
            message_content=MessageContent(request.content),
            message_date=MessageSendedAt(time_now)
        )
        await self.message_notification_repository.send_message(
            message_notification=notification_entity
        )