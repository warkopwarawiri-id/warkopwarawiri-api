import enum

class OrderStatus(enum.Enum):
    Cancel = 0
    Unconfirmed = 1
    InQueue = 2
    OnServing = 3
    Served = 4
    Paid = 5
    Complete = 6

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)