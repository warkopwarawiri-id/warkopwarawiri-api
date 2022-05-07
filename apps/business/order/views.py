from models.business.models import Business
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.request import Request
from rest_framework.response import Response
from usecases.order.business_order_data import business_order_data


class OrderViews:
    @api_view(["GET"])
    def main(request: Request, slug: str) -> Response:
        page = (
            int(request.query_params.get("page").strip())
            if request.query_params.get("page", "").isnumeric()
            else 1
        )
        limit = (
            int(request.query_params.get("limit").strip())
            if request.query_params.get("limit", "").isnumeric()
            else 10
        )

        if page < 1:
            page = 1

        if limit < 1:
            limit = 1
        elif limit > 100:
            limit = 100

        business = Business.objects.filter(slug=slug)
        if not business.exists():
            raise NotFound(detail="Business not found.")

        business = business.first()

        return business_order_data(slug=slug, page=page, limit=limit)
