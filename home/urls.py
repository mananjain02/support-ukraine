from django.urls import path, include
from . import views
# from allauth.account.urls

urlpatterns = [
    path('', views.SosView.as_view(), name='soshome'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('rescued', views.PeopleRescuedView.as_view(), name='rescued'),
    path('accounts/', include('allauth.urls')),
    path('lost-and-found/', include('lost_and_found.urls')),
    path('logout', views.LogOut, name='logout')
]