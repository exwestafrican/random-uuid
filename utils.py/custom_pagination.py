import rest_framework.pagination
from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data, **extra):
        return Response(
            {
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "count": self.page.paginator.count,
                "pages": self.page.paginator.num_pages,
                "success": True,
                "data": data,
                "extra": extra,
            }
        )
