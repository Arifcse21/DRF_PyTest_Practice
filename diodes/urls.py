from django.urls import path, include
from rest_framework.routers import DefaultRouter
from diodes.views import (
    CreateDiodeCategoryViewset,
    GetDiodeCategoryViewset,
)

router = DefaultRouter()

router.register('create-diode-cat', CreateDiodeCategoryViewset, basename='create_diode_cat')
# router.register('get-diode-cat', GetDiodeCategoryViewset, basename="get_diode_cat")


urlpatterns = [
    path("api/v1/diodes/", include(router.urls)),
    path("get-diode-cat/", GetDiodeCategoryViewset)
]
