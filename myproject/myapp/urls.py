
from statistics import StatisticsError
from tracemalloc import Statistic
from django.urls import path , include
from . import views 
from django.conf import settings
from django.conf.urls.static import static as statistics
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home , name = "home"),
    path("about/", views.about , name = "about"),
    path("login/", views.login_user , name = "login"),
    path("logout/", views.logout_user , name = "logout"),
    path("register/", views.register_user , name = "register"),
    path("product/<int:pk>", views.product_detail, name="product"),

    
    
    

] + statistics(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)