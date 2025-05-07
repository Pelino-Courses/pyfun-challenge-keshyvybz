from abc import ABC, abstractmethod

class NonEmptyString:
    def __init__(self, name: str):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{self.name[1:]} must be a non-empty string.")
        setattr(instance, self.name, value)

class Person(ABC):
    name = NonEmptyString("name")
    email = NonEmptyString("email")

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    @abstractmethod
    def get_role(self) -> str:
        pass
