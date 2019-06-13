from typing import Dict, Optional, get_args, get_origin, final


print(f"{get_origin(Dict[int, str]) = }")
print(f"{get_origin(Optional[Dict[int, str]]) = }")
print(f"{get_args(Optional[Dict[int, str]]) = }")

#######################################################################

# PEP 591


class Base:
    @final
    def done(self):
        print("Done")


class Derived(Base):
    def done(self):
        print("Not Done")

#######################################################################


@final
class Leaf:
    pass


class Other(Leaf):
    pass

#######################################################################


MAX_SIZE: Final = 9000
MAX_SIZE += 1  # Error reported by type checker


class Connection:
    TIMEOUT: Final[int] = 10


class FastConnector(Connection):
    TIMEOUT = 1  # Error reported by type checker

#######################################################################

# PEP 586


def validate_simple(data: Any) -> Literal[True]:  # always returns True
    return True


MODE = Literal['r', 'rb', 'w', 'wb']  # Could use Enum here too


def open_helper(file: str, mode: MODE) -> str:
    pass
