from django.contrib import admin

# Register your models here.

from .models import Origin, Category, Word

admin.site.register(Origin)
admin.site.register(Category)
admin.site.register(Word)
