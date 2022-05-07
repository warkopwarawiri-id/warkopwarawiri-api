import enum


class ProductCategories(enum.Enum):
    FOOD = "Food"
    BEVERAGE = "Beverage"
    OTHER = "Other"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
