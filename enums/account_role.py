import enum


class AccountRole(enum.Enum):
    DEVELOPER = "Developer"
    OWNER = "Owner"
    ADMIN = "Admin"
    STAFF = "Staff"
    INTERNAL = "Internal"
    GUEST = "Guest"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
