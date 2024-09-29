# store/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('create/', views.book_create, name='book_create'),
    path('update/<int:id>/', views.book_update, name='book_update'),
    path('delete/<int:id>/', views.book_delete, name='book_delete'),
    path('detail/<int:id>/', views.book_detail, name='book_detail'),

    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('registration_success/', views.registration_success, name='registration_success'),
    
    # URL สำหรับการจัดการรีเซ็ตรหัสผ่าน (Django Auth)
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='store/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='store/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='store/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='store/password_reset_complete.html'), name='password_reset_complete'),
]
