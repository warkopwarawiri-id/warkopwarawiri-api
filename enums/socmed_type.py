import enum


class SocmedType(enum.Enum):
    IG = "Instagram"
    FB = "Facebook"
    TW = "Twitter"
    YT = "Youtube"
    TKT = "Tiktok"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
