
from django.contrib import admin
from .models import *


class ColorAdmin(admin.ModelAdmin):
    list_display = ['color_name','color_code','color_tag']



class SizeAdmin(admin.ModelAdmin):
    list_display = ['size_name','size_code']


admin.site.register(category)
admin.site.register(product)
admin.site.register(product_image)
admin.site.register(color, ColorAdmin)
admin.site.register(size, SizeAdmin)
admin.site.register(variant)

