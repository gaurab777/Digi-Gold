from . import views
from django.urls import path

urlpatterns = [
    path('blog/frontpage/', views.frontpage, name='frontpage'),
	path('blog/<slug:slug>/', views.post_detail, name='post_detail'),
]
