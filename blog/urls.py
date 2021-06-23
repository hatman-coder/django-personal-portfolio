
from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
]
