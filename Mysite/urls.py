from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.create,name='create'),
    path('emp/',views.Emp,name='emp'),
    path('delete<id>/delete', views.delete_view,name='delete' ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


