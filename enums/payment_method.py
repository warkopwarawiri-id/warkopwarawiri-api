import enum


class PaymentMethod(enum.Enum):
    CASH = "Cash"
    OTHER = "Other"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
