from django.contrib import admin
from diodes.models import Diode, DiodeCategory
# Register your models here.


@admin.register(Diode)
class DiodeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "diode_name",
        "diode_category",
        "diode_characteristics",
        "created_at",
        "modified_at"
    ]


@admin.register(DiodeCategory)
class DiodeCategoryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "category",
        "description",
        "created_at",
        "updated_at"
    ]