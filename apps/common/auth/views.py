from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from utils.api_response import ApiResponse


class AuthView:
    @staticmethod
    @api_view(["GET", "POST"])
    def main(request: Request) -> Response:
        return ApiResponse()
