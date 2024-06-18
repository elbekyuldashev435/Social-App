from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [

    # auth
    path('registration/', views.Registration.as_view(), name="registration"),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),

    # profile
    path('my_profile/<int:pk>/', views.MyProfile.as_view(), name='my_profile'),
    path('edit_my_profile/<int:pk>/', views.EditProfile.as_view(), name='edit_my_profile'),
    path('profile/<int:pk>/', views.Profile.as_view(), name='profile'),

    path('add-contact/<int:pk>/', views.AddContactView.as_view(), name='add-contact'),
]

"""
    READ ME BEFORE YOU USE ME |

    my_profile - o'zini profilini ko'radi va edit qilishga permissioni bor
    profile - boshqa akkauntlarning profili uni edit qilib bo'lmaydi
    
    O'zini profiliga jo'natmoqchi bo'lsak my_profilega url beramiz
    Agar birovni profilini ko'rmoqchi bo'lsak profile ga url beramiz

"""