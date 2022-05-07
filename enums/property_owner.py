import enum


class PropertyOwner(enum.Enum):
    USER = "account"
    BUSINESS = "business"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
