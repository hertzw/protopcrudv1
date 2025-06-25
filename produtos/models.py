from datetime import date
from django.db import models
from django.core.exceptions import ValidationError
   
class Produto(models.Model):
    title = models.CharField(
        verbose_name="Título", max_length=100, null=False, blank=False
    )
    line = models.CharField(max_length=50, default='temp line')
    scale = models.CharField(max_length=10)
    vendor = models.CharField(max_length=50, default='temp vendor')
    description = models.CharField(max_length=100, default='temp descr')
    quantity_in_stock = models.IntegerField(default=0, null=False)
    buy_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    msrp = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    finished_at = models.DateField(null=True)

    class Meta:
        ordering = ["title"]
    def mark_has_complete(self):
        if not self.finished_at:
             self.finished_at = date.today()
             self.save()
    def save(self, *args, **kwargs):
        limite = 15  # Defina o limite desejado
        if not self.pk and Produto.objects.count() >= limite:
            raise ValidationError(f"Você só pode ter {limite} registros no total.")
        super().save(*args, **kwargs)