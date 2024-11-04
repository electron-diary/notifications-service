import logging
from faststream.nats.annotations import NatsBroker as Broker
from faststream.nats.broker import NatsBroker

from app.infrastructure.broker.config import NatsConfig


def get_broker(nats_config: NatsConfig) -> Broker:
    nats_broker: Broker = NatsBroker(
        servers=[nats_config.nats_uri],
        log_level=logging.INFO
    )
    return nats_broker