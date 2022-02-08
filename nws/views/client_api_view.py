import os
import requests
from django.core.cache import cache
from django.http import JsonResponse
from dotenv import load_dotenv
from rest_framework import status
from rest_framework.views import APIView

from ..utility import Utility

load_dotenv()


class ClientAPIView(APIView):
    """
    This Class handes nws report endpoints
    """
    def get(self, request):
        """
        Handles get request, validates request and send report in response
        """
        station_code = request.GET.get("scode")
        no_cache = request.GET.get("nocache", None)
        http_status = status.HTTP_200_OK
        if (station_code in cache and no_cache and no_cache != "1") or (station_code in cache and not no_cache):
            data = cache.get(station_code)
        else:
            response = requests.get(f"{os.environ['BASE_URL']}{station_code}.TXT")
            if response.status_code == 200:
                try:
                    data = Utility.string_to_json(response.content.decode("utf-8"))
                    cache.set(station_code, data, timeout=300)
                except:
                    data = {"Request": "Data Invalid"}
            else:
                data = {"Request": "Not Found"}
                http_status = status.HTTP_400_BAD_REQUEST
                
        return JsonResponse(data, safe=False, status=http_status)
