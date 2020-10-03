from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.homePage.as_view(),name='home'),
    path('about/',views.aboutPage.as_view(),name='about'),
    path('contact/',views.contactPage.as_view(),name='contact'),
]
