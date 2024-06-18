from django.urls import path
from . import views


urlpatterns = [

    # auth
    path('registration/', views.Registration.as_view(), name="registration"),
    path('login/', views.Login.as_view(), name='login'),

    # profile
    path('my_profile/<int:pk>/', views.MyProfile.as_view(), name='my_profile'),
    path('edit_my_profile/<int:pk>/', views.EditProfile.as_view(), name='edit_my_profile'),
]
