from django.db import models


def maintain_serial():
    last_entry = DiodeCategory.objects.all().order_by('id').last()
    if last_entry:
        return last_entry.id + 1
    return 1


class DiodeCategory(models.Model):
    id = models.AutoField(unique=True, primary_key=True, editable=False, default=maintain_serial)
    category = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Diode Categories"
        app_label = "diodes"

    def __str__(self):
        return str(self.category)
