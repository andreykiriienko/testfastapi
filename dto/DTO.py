from dataclasses import dataclass, field

@dataclass()
class Users:
    id: int = field(default_factory=int)
    username: str = field(default='')
    age: int = field(default_factory=int)
    email: str = field(default='')


@dataclass()
class Games:
    id: int = field(default_factory=int)
    name: str = field(default='')
