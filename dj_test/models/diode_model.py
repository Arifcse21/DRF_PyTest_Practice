from django.db import models


class Diode(models.Model):
    diode_name = models.CharField(max_length=100, null=True, blank=True)
    diode_model = models.CharField(max_length=100, null=True, blank=True)
    diode_type = models.CharField(max_length=100, null=True, blank=True)
    diode_characteristics = models.CharField(max_length=200, null=True, blank=True)
    diode_symbol = models.ImageField(upload_to="/diodes", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.diode_name)
