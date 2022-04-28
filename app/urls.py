from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app import views

urlpatterns =[
    path('user/',views.UserList.as_view()),
    path('users/<int:pk>/',views.UserDetail.as_view()),
    path('list/',views.ListList.as_view()),
    path('lists/<int:pk>/',views.ListDetail.as_view()),
    path('item/',views.ItemList.as_view()),
    path('items/<int:pk>/',views.ItemDetail.as_view()),
    path('category/',views.CategoryList.as_view()),
    path('categorys/<int:pk>/',views.CategoryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)