from django.contrib import admin
from .models import *



admin.site.register(category)
admin.site.register(product)
admin.site.register(product_image)
admin.site.register(color)
admin.site.register(size)
admin.site.register(variant)

