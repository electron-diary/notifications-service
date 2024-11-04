from typing import Self, Protocol
from abc import abstractmethod


class Interactor[Request, Response](Protocol):
    @abstractmethod
    async def __call__(self: Self, request: Request) -> Response:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )