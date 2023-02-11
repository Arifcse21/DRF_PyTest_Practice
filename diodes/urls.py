from django.urls import path, include
from rest_framework.routers import DefaultRouter
from diodes.views import (
    CreateDiodeCategoryViewset
)

router = DefaultRouter()

router.register('create-diode-cat', CreateDiodeCategoryViewset, basename='create_diode_cat')


urlpatterns = [
    path("api/v1/diode/", include(router.urls)),
]