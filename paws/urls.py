from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # This is all the paws
    path('<int:paws_id>/comment',views.comment, name='comment')    

]