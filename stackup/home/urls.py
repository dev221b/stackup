from django.urls import path
from.import views 

urlpatterns = [
    path('', views.index , name = "index"),
    path('signup', views.signupp , name = "signup"),
    path('login', views.loginn , name = "login"),
    path('landingpage', views.landingPage , name = "landingpage"),
]