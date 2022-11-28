from django.contrib import admin
from django.urls import path
from glue import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/cv',views.home, name='home'),
    path('resume',views.resume, name='resume'),
    path('home',views.demo, name='demo'),
    path('user/signup',views.signup,name='usign'),
    path('logout',views.logout_view,name="out"),
    path('',views.login,name='ulog'),
    path('delete',views.r_delet,name="de"),


]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)