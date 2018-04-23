from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # This is all the paws
    path('<int:paws_id>/comment',views.comment, name='comment'),
    path ('writePaws/', views.writePaws, name='writePaws') ,
    path ('login/' , views.login, name='login'),
    path ('logout/',views.logout_view, name='logout'),
    path('yourPaws/', views.yourPaws, name="yourPaws"),
    path('register/',views.register, name='register'),
    path('follow_up/', views.follow_Up_View, name='followUp')
]