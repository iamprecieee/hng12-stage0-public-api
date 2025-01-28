from rest_framework.views import APIView
from .serializer import DataSerializer
from drf_spectacular.utils import extend_schema
import os
from datetime import datetime, timezone
from rest_framework.response import Response
from rest_framework import status


class DataView(APIView):
    serializer_class = DataSerializer

    @extend_schema(operation_id="v1_data", tags=["data_v1"])
    def get(self, request):
        try:
            raw_data = {
                "email": os.getenv("EMAIL_VALUE"),
                "current_datetime": datetime.now(timezone.utc).isoformat(),
                "github_url": os.getenv("GITHUB_URL"),
            }
            response_data = self.serializer_class(raw_data).data
            return Response(data=response_data, status=status.HTTP_200_OK)
        except Exception as e:
            print(str(e))
            return Response(
                data="Internal error. Dev was probably drunk⚠️",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
