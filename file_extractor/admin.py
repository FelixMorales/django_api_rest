from .models import NEREntityTag, Document, NEREntity
from django.contrib import admin

admin.site.register(NEREntityTag)
admin.site.register(Document)
admin.site.register(NEREntity)