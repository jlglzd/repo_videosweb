#from django.conf.urls import url

from django.urls import path

from django.urls import re_path as url

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('videos/', views.BookListView.as_view(), name='videos'),
	path('video/<int:pk>', views.BookDetailView.as_view(), name='video-detail'),
]
