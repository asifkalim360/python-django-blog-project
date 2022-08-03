from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from first_blog_app import views

urlpatterns = [
    path('',views.home, name="home"),
    path('<slug:url>', views.posts, name="posts"),
    path('<slug:url>', views.category, name="category"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
