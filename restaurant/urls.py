from django.urls import path
from .views import Homepage, Menupage, Contactpage, Reviewpage, ContactReport, FeedbackDelete

urlpatterns = [
    path('', Homepage, name='homepage'),
    path('menu/', Menupage, name='menupage'),
    path('contact/',Contactpage, name='contactpage'),
    path('review/',Reviewpage, name='reviewpage'),
    path('contactreport/',ContactReport, name='contactreport'),
    path('feedbackdelete/<int:pk>/', FeedbackDelete, name='feedbackdelete')
]
