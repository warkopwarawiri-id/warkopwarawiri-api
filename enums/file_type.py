import enum


class FileType(enum.Enum):
    IMAGE = "Image"
    OTHER = "Other"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
