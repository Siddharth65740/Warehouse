from django.db import models
from django.urls import reverse

class inducts(models.Model):
    shipment=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.shipment},{self.destination}"

class induct_2(models.Model):
    shipment_1 = models.CharField(max_length=100)
    destination_1 = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.shipment_1},{self.destination_1}"