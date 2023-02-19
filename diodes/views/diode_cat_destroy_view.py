from drf_yasg.utils import swagger_auto_schema
from .diode_cat_retrieve_view import DiodeCatRetrieveViewSet
from rest_framework.response import Response
from rest_framework import status
from diodes.models import DiodeCategory
from diodes.serializers import DiodeCategorySerializer


class DiodeCatDestroyViewSet(DiodeCatRetrieveViewSet):

    @swagger_auto_schema(
        operation_summary="Delete/Destroy category",
        operation_description="Delete a category from database using the primary key"
    )
    def destroy(self, request, pk=None):

        try:
            queryset = DiodeCategory.objects.filter(pk=pk).delete()
            if not queryset[0]:
                api_response = {
                    "successful": False,
                    "message": f"Category no.{pk} doesn't exists"
                }
                return Response(api_response, status=status.HTTP_404_NOT_FOUND)
            api_response = {
                "successful": True,
                "message": f"category deleted successfully"
            }
            return Response(api_response, status=status.HTTP_200_OK)
        except Exception as e:
            api_response = {
                "successful": False,
                "message": str(e)
            }
            return Response(api_response, status=status.HTTP_400_BAD_REQUEST)
