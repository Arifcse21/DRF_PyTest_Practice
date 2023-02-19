import json
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from diodes.views import (
    CreateDiodeCategoryViewSet,
    GetDiodeCategoryViewSet,
    DiodeCatDestroyViewSet
)
endpoints_file = open("endpoints_config.json")
endpoints = json.load(endpoints_file)

router = DefaultRouter()

# Diode Category
router.register(endpoints["create_diode_cat"], CreateDiodeCategoryViewSet, basename='create-diode-cat')
router.register(endpoints["get_diode_cat"], GetDiodeCategoryViewSet, basename="get-diode-cat")
router.register(endpoints["ret_del_diode_cat"], DiodeCatDestroyViewSet, basename="ret-del-diode-cat")

# Diode Record

urlpatterns = [
    path(endpoints["base_url"], include(router.urls)),
]
