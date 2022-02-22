from django.contrib import admin
from .models import Category,Review,Restaurant



class RestaurantAdmin(admin.ModelAdmin):
    list_display    = ["name","description","category","dt","prefecture","city","address","image","lat","lon","ip","judge_dt"]



admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Restaurant,RestaurantAdmin)


