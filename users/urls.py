from django.urls import path
from . import views


urlpatterns = [

    # auth
    path('registration/', views.Registration.as_view(), name="registration"),
    path('login/', views.Login.as_view(), name='login'),

    # profile
    path('my_profile/<int:pk>/', views.MyProfile.as_view(), name='my_profile'),
    path('edit_my_profile/<int:pk>/', views.EditProfile.as_view(), name='edit_my_profile'),
    path('profile/<int:pk>/', views.Profile.as_view(), name='profile')
]

"""
    READ ME BEFORE YOU USE ME |

    my_profile - o'zini profilini ko'radi va edit qilishga permissioni bor
    profile - boshqa akkauntlarning profili uni edit qilib bo'lmaydi
    
    O'zini profiliga jo'natmoqchi bo'lsak my_profilega url beramiz
    Agar birovni profilini ko'rmoqchi bo'lsak profile ga url beramiz

"""