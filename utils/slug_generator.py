from django.utils.text import slugify


def slug_generator(source: str, model: object = None):
    slug = slugify(value=source, allow_unicode=False)

    if model is not None:
        is_deleted_field = hasattr(model, "is_deleted")

        if is_deleted_field:
            if not model.default_objects.fiter(slug=slug).exists():
                return slug
            else:
                i = 0
                while model.default_objects.fiter(slug=f"slug{str(i)}").exists():
                    i += 1

                return f"slug{str(i)}"
        else:
            if not model.objects.fiter(slug=slug).exists():
                return slug
            else:
                i = 0
                while model.objects.fiter(slug=f"slug{str(i)}").exists():
                    i += 1

                return f"slug{str(i)}"

    else:
        return slug
