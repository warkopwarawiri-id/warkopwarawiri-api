import enum

class AccountRole(enum.Enum):
    Developer = 'dev'
    Owner = 'owner'
    Administrator = 'admin'
    Staff = 'staff'
    Guest = 'guest'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)