from typing import Protocol, runtime_checkable


@runtime_checkable
class Protobuf(Protocol):
    def decode(self, string: str) -> None:
        pass


class MyMessage:
    def decode(self, string: str) -> None:
        pass


assert isinstance(MyMessage(), Protobuf)
