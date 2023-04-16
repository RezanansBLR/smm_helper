from django.contrib import admin
from .models import Bloger

class BlogerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("username",)}

admin.site.register(Bloger, BlogerAdmin)
