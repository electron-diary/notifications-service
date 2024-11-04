from dataclasses import dataclass


@dataclass(frozen=True)
class SendEmailNotificationRequestDto:
    content: str
    subject: str
    email: str