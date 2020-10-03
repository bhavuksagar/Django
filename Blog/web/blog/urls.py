from django.urls import path
from . import views
urlpatterns = [
    path('', views.homePage.as_view(),name='home'),
    path('blog/<int:pk>',views.detailPage.as_view(),name='detail'),
    path('blog/<int:pk>/update',views.editPage.as_view(),name='edit'),
    path('new-blog/',views.Create.as_view(),name='new'),
]
