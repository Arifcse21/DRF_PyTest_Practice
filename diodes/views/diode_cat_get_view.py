from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from diodes.serializers import DiodeCategorySerializer
from diodes.models import DiodeCategory
from drf_yasg.utils import  swagger_auto_schema


class GetDiodeCategoryViewset(ViewSet):

    @swagger_auto_schema(
        operation_summary="Get all diode categories",
        operation_description="This api returns all categories for diodes"
    )
    def list(self, request):
        try:
            queryset = DiodeCategory.objects.all()
            serializer = DiodeCategorySerializer(queryset, many=True)

            api_response = {
                "successful": True,
                "message": "Diode Category List",
                "data": serializer.data
            }
            return Response(api_response, status=status.HTTP_200_OK)

        except Exception as e:
            api_response = {
                "successful": False,
                "message": str(e)
            }
            return Response(api_response, status=status.HTTP_400_BAD_REQUEST)
