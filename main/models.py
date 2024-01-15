from django.db import models
from enum import Enum

class Category(Enum):
    MONERA = 'Monera'
    PROTIST = 'Protist'
    FUNGI = 'Fungi'
    PLANTAE = 'Plantae'
    ANIMALIA = 'Animalia'
    RANDOM = 'Random/Unidentified'

class Tag(models.Model):
    name = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.name
    

class Content(models.Model):
    category = models.CharField(
        max_length=20,
        choices=[(tag.name, tag.value) for tag in Category],
        default=Category.RANDOM
    )
    name = models.CharField(default='', max_length=255)
    latin_name = models.CharField(default='', max_length=255)
    resource = models.URLField()
    location_found = models.CharField(default='', max_length=255)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
