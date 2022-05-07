import enum


class CategoryType(enum.Enum):
    HOT_DRINK = "Hot Drink"
    COLD_DRINK = "Cold Drink"
    SNACK = "Snack"
    DESSERT = "Dessert"
    MAIN_COURSE = "Main Course"
    OTHER = "Other"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
