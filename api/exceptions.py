import logging
import traceback
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)

def custom_exception_handler(exc, context):
    """
    Custom exception handler for Django REST Framework.
    """
    response = exception_handler(exc, context)

    if response is None:
        # If DRF doesn't handle the exception, handle it here
        logger.error(f"Unhandled Exception: {str(exc)}")
        logger.error(traceback.format_exc())

        return Response(
            {
                "error": "Something went wrong",
                "detail": str(exc)  # Hide this in production for security
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return response
