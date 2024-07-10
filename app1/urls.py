from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('profile', views.profile, name='profile'),
    path('update', views.update, name='update'),

    path('', views.index, name='index'),
    path('aboutus', views.aboutus, name='about'),
    path('profile', views.profile, name='profile'),
    path('leaderboard', views.leaderboard, name='leader'),
    path('ques', views.ques, name='ques'),
    path('show/<str:pk>/', views.show, name='show'),
    path('check/<str:pk>/', views.check, name='check'),
]