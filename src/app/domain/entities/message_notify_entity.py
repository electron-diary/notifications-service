from dataclasses import dataclass

from app.domain.value_objects.message_notify.message_content_value_object import MessageContent
from app.domain.value_objects.message_notify.message_sended_at_value_object import MessageSendedAt
from app.domain.value_objects.message_notify.phone_number_value_object import PhoneNumber
from app.domain.common.entity import DomainEntity


@dataclass
class MessageNotificationEntity(DomainEntity[PhoneNumber]):
    contact: PhoneNumber
    message_content: MessageContent
    message_date: MessageSendedAt
