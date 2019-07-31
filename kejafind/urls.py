from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name='home'),
    path('<int:blog_id>/', blog.views.detail, name='detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
