from django.contrib import admin
from .models import Categories
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('categories_name',)}
    list_display = ('categories_name','slug','created_date',)


admin.site.register(Categories,CategoryAdmin)