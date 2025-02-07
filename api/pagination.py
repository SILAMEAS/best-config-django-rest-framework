from rest_framework.pagination import (PageNumberPagination)
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    page_query_param='page'
    max_page_size = 20
    def get_paginated_response(self, data):
        return Response({
            'hasNext':self.page.has_next(),
            'currentPage':self.page.number,
            'total': self.page.paginator.count,
            'contents': data,
            'totalPages': self.page.paginator.num_pages,
        })
    
    # pagination_class = LimitOffsetPagination    # http://localhost:8000/products/?limit=2&offset=8