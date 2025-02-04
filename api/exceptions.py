from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    """
    Custom exception handler similar to @ControllerAdvice in Spring Boot.
    """
    response = exception_handler(exc, context)

    # If response is None, it means DRF didn't handle the exception, so we handle it
    if response is None:
        return Response(
            {"error": str(exc)},  # Generic error message
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    # Customize the response data if needed
    response.data['status_code'] = response.status_code
    return response
