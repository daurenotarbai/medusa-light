from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.main_view, name='main'),

    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),

    path('news/admin', views.ArticleView.as_view(), name='articles'),
    path('news/', views.ArticleAPIView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
