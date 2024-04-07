from django.db import models

# Create your models here.

#* To create Manager of something (1)
class CarWithImageManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(image = "") #* images is like home/leo/img

class Car(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()

    #* (2)
    objects = models.Manager()
    with_images = CarWithImageManager()
