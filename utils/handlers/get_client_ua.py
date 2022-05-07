from rest_framework.request import Request


def get_client_ua(request: Request) -> str:
    return request.META.get("HTTP_USER_AGENT")
