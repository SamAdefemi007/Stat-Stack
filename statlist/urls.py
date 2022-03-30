from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('profile', views.profile, name="profile"),
    path('profile/<int:id>/', views.details, name="details"),
    path('country', views.country, name="country"),
    path('club', views.club, name="club"),
    path('compare', views.compare, name="compare"),

]
