from django.urls import path

from . import views

urlpatterns = [    
    path('', views.user_list, name='users'),
    path('<int:id>/', views.user_detail, name='users id'),
]
