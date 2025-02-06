from rest_framework.pagination import (PageNumberPagination)
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param='page'
    max_page_size = 20
    def get_paginated_response(self, data):
        # print(self.page.)
        return Response({
            'hasNext':self.page.has_next(),
            'currentPage':self.page.number,
            'totals': self.page.paginator.count,
            'data': data
        })
    
    # pagination_class = LimitOffsetPagination    # http://localhost:8000/products/?limit=2&offset=8