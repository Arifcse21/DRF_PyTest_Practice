from django.db import models


class DiodeCategory(models.Model):
    category = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Diode Categories"
        app_label = "diodes"

    def __str__(self):
        return str(self.category)
