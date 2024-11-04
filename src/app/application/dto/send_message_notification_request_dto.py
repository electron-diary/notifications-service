from dataclasses import dataclass


@dataclass(frozen=True)
class SendMessageNotificationRequestDto:
    content: str
    phone_number: str