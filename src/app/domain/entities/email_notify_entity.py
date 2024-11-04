from dataclasses import dataclass

from app.domain.value_objects.email_notify.email_content_value_object import EmailContent
from app.domain.value_objects.email_notify.email_sended_at_value_object import EmailSendAt
from app.domain.value_objects.email_notify.email_value_object import Email
from app.domain.value_objects.email_notify.email_subject_value_object import EmailSubject
from app.domain.common.entity import DomainEntity


@dataclass
class EmailNotificationEntity(DomainEntity[Email]):
    contact: Email
    email_subject: EmailSubject
    email_date: EmailSendAt
    email_content: EmailContent
