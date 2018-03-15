from django.contrib import admin
from HotPotWebsite.models import MenuCategory, Dish, UserProfile

# Register your models here.

admin.site.register(UserProfile)

class MenuCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


admin.site.register(MenuCategory, MenuCategoryAdmin)


class DishAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price')


admin.site.register(Dish, DishAdmin)