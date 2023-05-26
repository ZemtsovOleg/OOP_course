from dataclasses import dataclass, field


@dataclass(order=True)
class User:
    name: str = field(compare=False)
    age: int
    rating: float


bob = User('Bob', 25, 101)
ash = User('Ash', 26, 100)
print(ash > bob)
