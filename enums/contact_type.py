import enum


class ContactType(enum.Enum):
    PHONE = "Phone"
    WHATSAPP = "Whatsapp"
    EMAIL = "Email"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
