from django.contrib import admin
from .models import HeroSection, SpecialHeader, SpecialItem, ServiceSection, Services, FavoriteHeader, FavItem, LatestMenu, Menu, CustomerFeedback, Feedback, Contact, Branches
# Register your models here.

models_list = [
    HeroSection, SpecialHeader, SpecialItem, ServiceSection, Services,
    FavoriteHeader, FavItem, LatestMenu, Menu, CustomerFeedback,
    Feedback, Contact, Branches
]

admin.site.register(models_list)    