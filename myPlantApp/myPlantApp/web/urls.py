from django.urls import path

from myPlantApp.web.views import home_page, create_profile, catalogue, create_plant, details_plant, edit_plant, \
    delete_plant, details_profile, edit_profile, delete_profile

urlpatterns = [
    path('', home_page, name='index'),
    path('profile/create/', create_profile, name='create profile'),
    path('catalogue/', catalogue, name='catalogue'),
    path('create/', create_plant, name='create plant'),
    path('details/<int:pk>/', details_plant, name='details plant'),
    path('edit/<int:pk>/', edit_plant, name='edit plant'),
    path('delete/<int:pk>/', delete_plant, name='delete plant'),
    path('profile/details/', details_profile, name='details profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
]
