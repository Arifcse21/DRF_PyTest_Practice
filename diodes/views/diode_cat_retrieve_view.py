from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from diodes.models import DiodeCategory
from diodes.serializers import DiodeCategorySerializer


class DiodeCatRetrieveViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary="Retrieve individual diode category",
        operation_description="This api returns individual category for diodes using primary key"
    )
    def retrieve(self, request, pk=None):
        try:
            queryset = DiodeCategory.objects.filter(pk=pk)

            serializer = DiodeCategorySerializer(queryset.first())
            api_response = {
                "successful": True,
                "message": "individual diode category data",
                "data": serializer.data
            }
            return Response(api_response, status=status.HTTP_200_OK)
        except Exception as e:
            api_response = {
                "successful": False,
                "message": str(e)
            }
            return Response(api_response, status=status.HTTP_400_BAD_REQUEST)

