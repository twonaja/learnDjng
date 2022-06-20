from django.db import models


class Car(models.Model):
    brand_of_car = models.CharField(max_length=50)
    model_of_car = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    date_create = models.CharField(max_length=10)

    def __str__(self):
        return self.brand_of_car + ' ' + self.model_of_car
