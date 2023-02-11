from rest_framework.serializers import ModelSerializer
from diodes.models import DiodeCategory


class DiodeCategorySerializer(ModelSerializer):

    class Meta:
        model = DiodeCategory
        fields = "__all__"


