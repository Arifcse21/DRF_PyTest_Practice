from django.contrib import admin
from diodes.models import Diode
# Register your models here.

@admin.register(Diode)
class DiodeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "diode_name"
    ]
