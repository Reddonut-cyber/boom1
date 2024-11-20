from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_view, name='input'),  # URL สำหรับฟอร์ม
    path('success/', views.success_view, name='success'),  # URL สำหรับหน้า success
]
