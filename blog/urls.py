from django.urls import path
from .views import (
    BlogListView,
    BlogUpdateView,
    BlogDetailView,
    BlogDeleteView,
    BlogCreateView,
)


urlpatterns = [
path('<int:pk>/edit/',BlogUpdateView.as_view(), name='post_edit'), 
path('<int:pk>/',BlogDetailView.as_view(), name='post_detail'), 
path('<int:pk>/delete/',BlogDeleteView.as_view(), name='post_delete'),
path('<int:pk>/new/', BlogCreateView.as_view(),name = 'post_new'),
path('', BlogListView.as_view(), name='post_list'),

]
