from django.contrib import admin
from . import models

class ArticleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Article._meta.fields]

admin.site.register(models.Article, ArticleAdmin)
