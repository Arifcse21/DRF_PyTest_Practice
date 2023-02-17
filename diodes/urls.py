import json
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from diodes.views import (
    CreateDiodeCategoryViewset,
    GetDiodeCategoryViewset,
)
endpoints_file = open("endpoints_config.json")
endpoints = json.load(endpoints_file)

router = DefaultRouter()

router.register(endpoints["create_diode_cat"], CreateDiodeCategoryViewset, basename='create-diode-cat')
router.register(endpoints["get_diode_cat"], GetDiodeCategoryViewset, basename="get-diode-cat")


urlpatterns = [
    path(endpoints["base_url"], include(router.urls)),
]
