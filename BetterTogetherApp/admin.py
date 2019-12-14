from django.contrib import admin
from .models import Info, ShareFood, SharePromotion, ShareRide
# Register your models here.

admin.site.register(Info)
admin.site.register(ShareFood)
admin.site.register(ShareRide)
admin.site.register(SharePromotion)