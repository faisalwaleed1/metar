from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class StatusAPIView(APIView):
    """
    This class handles status api endpoints.
    """
    permission_classes = (AllowAny,)
    def get(self, request):
        """
        Handle GET request, return API status.
        """
        return JsonResponse({"data": "pong"}, safe=False, status=status.HTTP_200_OK)
