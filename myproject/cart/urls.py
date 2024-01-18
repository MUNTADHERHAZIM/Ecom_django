from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.cart_summary, name="cart_summary"),
    path("add/", views.cart_add, name="cart_add"),
    path("delete/", views.cart_delete, name="cart_delete"),
    path("update/", views.cart_update, name="cart_update"),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)