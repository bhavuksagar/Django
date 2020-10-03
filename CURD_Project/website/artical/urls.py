from django.urls import path
from . import views
urlpatterns = [
    path("",views.homePage.as_view(),name='homepage'),
    path('artical/<int:pk>',views.detailPage.as_view(),name='detail'),
    path('new/',views.createview.as_view(),name='createview'),
    path('artical/<int:pk>/update',views.edit.as_view(),name='edit'),
    path('artical/<int:pk>/delete',views.delete.as_view(),name='art_delete'),

]
