from . import views
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.home, name='home'),
 path('add_blog/', views.add_blog, name='add_blog'),
    path('addblog/<str:pk>/', views.addblog), 
    path('delete_blog/<int:pk>/', views.delete_blog, name='delete_blog'),
     path('update_blog/<int:pk>/', views.update_blog, name='update_blog'),
] 
if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
