from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from diodes.models import DiodeCategory
from diodes.serializers import CreateDiodeCategorySerializer


class CreateDiodeCategoryViewset(ViewSet):

    def create(self, request):
        print("category data = ", request.data)

        diode_cat_record = {
            "category": request.data["category"],
            "description": request.data["description"]
        }

        try:

            serializer = CreateDiodeCategorySerializer(data=diode_cat_record, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()

            api_response = {
                "successful": True,
                "message": "New diode category created",
                "data": serializer.data
            }
            return Response(api_response, status=status.HTTP_201_CREATED)
        except Exception as e:
            api_response = {
                "successful": False,
                "message": str(e)
            }
            return Response(api_response, status=status.HTTP_400_BAD_REQUEST)
