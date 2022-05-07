import enum


class PaymentStatus(enum.Enum):
    FAILED = 0
    WAITING = 1
    NEED_CONFIRM = 2
    CONFIRMED = 3

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
