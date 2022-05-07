from rest_framework.views import exception_handler
from utils.api_response import ApiResponse


def custom_exception(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response = ApiResponse(response.data.get("detail"), response.status_code)

    return response
