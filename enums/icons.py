import enum


class Icons(enum.Enum):
    FACEBOOK = ""
    INSTAGRAM = ""
    PHONE = ""
    EMAIL = ""
    WHATSAPP = ""
    TIKTOK = ""
    YOUTUBE = ""
    TWITTER = ""

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
