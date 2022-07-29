from django.contrib import admin

from .models import User,Sell,Buyer

admin.site.register(User)

admin.site.register(Sell)

admin.site.register(Buyer)