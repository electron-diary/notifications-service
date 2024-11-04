from typing import Self
from datetime import datetime

from app.domain.entities.email_notify_entity import EmailNotificationEntity
from app.domain.repositories.email_notify_repository import EmailNotificationRepository
from app.domain.value_objects.email_notify.email_content_value_object import EmailContent
from app.domain.value_objects.email_notify.email_value_object import Email
from app.domain.value_objects.email_notify.email_sended_at_value_object import EmailSendAt
from app.domain.value_objects.email_notify.email_subject_value_object import EmailSubject
from app.application.interfaces.interactor import Interactor
from app.application.dto.send_email_notification_request_dto import SendEmailNotificationRequestDto


class SendEmailNotificationUseCase(Interactor[SendEmailNotificationRequestDto, None]):
    def __init__(self: Self, email_notifications_repository: EmailNotificationRepository) -> None:
        self.email_notification_repository: EmailNotificationRepository = email_notifications_repository

    async def __call__(self: Self, request: SendEmailNotificationRequestDto) -> None:
        time_now: datetime = datetime.now()
        notification_entity: EmailNotificationEntity = EmailNotificationEntity(
            contact=Email(request.email),
            email_subject=EmailSubject(request.subject),
            email_content=EmailContent(request.content),
            email_date=EmailSendAt(time_now)
        )
        await self.email_notification_repository.send_email(
            email_notification=notification_entity
        )