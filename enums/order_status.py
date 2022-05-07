import enum


class OrderStatus(enum.Enum):
    CANCEL = 0
    UNCONFIRMED = 1
    IN_QUEUE = 2
    ONSERVING = 3
    SERVED = 4
    PAID = 5
    COMPLETE = 6

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
