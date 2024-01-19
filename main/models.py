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

class Like(models.Model):
    ip_address = models.CharField(max_length=15)
    is_like = models.BooleanField(default=False)

class Comment(models.Model):
    comment = models.TextField(default='')

class Content(models.Model):
    category = models.CharField(
        max_length=20,
        choices=[(tag.name, tag.value) for tag in Category],
        default=Category.RANDOM
    )
    name = models.CharField(max_length=255)
    latin_name = models.CharField(default='Unknown', max_length=255)
    resource = models.URLField()
    location_found = models.CharField(default='Unknown', max_length=255)
    description = models.TextField(default='')
    tags = models.ManyToManyField(Tag, blank=True)
    likes = models.ManyToManyField(Like, blank=True)
    comment = models.ManyToManyField(Comment, blank=True)

    def __str__(self):
        return self.name
