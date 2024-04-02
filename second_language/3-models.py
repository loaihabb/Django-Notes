from django.db import models

# Create your models here.

class Object(models.Model):
    title = models.CharField(max_length=100)
    title_ar = models.CharField(max_length=100) #* Added the second language
    image = models.ImageField()
    description = models.TextField()
    description_ar = models.TextField() #* second language

    def __str__(self):
        return self.title # * Any Object in the database will take this, when deleting or showing etc...

    class Meta:
        ordering = ["-title"]