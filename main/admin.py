from django.contrib import admin
from main.models import Content, Tag, Like, Comment

admin.site.register(Content)
admin.site.register(Tag)
admin.site.register(Like)
admin.site.register(Comment)