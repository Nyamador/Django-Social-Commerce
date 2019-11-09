from django.urls import path
from pages import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('feed/', views.feed, name="feed"),
]
