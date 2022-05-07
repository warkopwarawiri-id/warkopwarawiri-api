from models.business.models import Business
from rest_framework.response import Response
from utils.api_response import ApiResponse


def business_order_data(business: Business, page: int, limit: int) -> Response:

    return ApiResponse()
