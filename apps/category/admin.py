from django.contrib import admin

from apps.category.models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)
    list_per_page = 25
    
admin.site.register(Category, CategoryAdmin)
