from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)


class Person(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='person/images', default='person/default.png')
    job = models.ForeignKey('apps.Category', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
