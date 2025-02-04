from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    # Handle specific exception
    if isinstance(exc, ObjectDoesNotExist):
        return Response(
            {"error": "The requested resource was not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    # Add more specific exception handling as needed
    if response is None:
        return Response(
            {"error": "An unexpected error occurred."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    # Customize the default response
    response.data['status_code'] = response.status_code
    return response
