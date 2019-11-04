from django.contrib import admin
from .models import User, ShareFood, SharePromotion, ShareRide
# Register your models here.

admin.site.register(User)
admin.site.register(ShareFood)
admin.site.register(ShareRide)
admin.site.register(SharePromotion)