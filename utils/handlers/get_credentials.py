from rest_framework.request import Request


def get_credentials(request: Request) -> str:
    try:
        return request.headers.get("Authorization").strip().split("Bearer ")[1]
    except:
        return None
