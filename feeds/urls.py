from django.urls import path
from . import views

app_name = 'feeds'

urlpatterns = [
    path('', views.index, name='index'),
    ## Feed - Create Read(detail) Update Delete
    path('create/', views.create, name='create'),
    path('<int:feed_pk>/detail/', views.detail, name='detail'),
    path('<int:feed_pk>/update/', views.update, name='update'),
    path('<int:feed_pk>/delete/', views.delete, name='delete'),
    path('<int:feed_pk>/like/', views.like, name='like'),
    path('<int:feed_pk>/bookmark/', views.bookmark, name='bookmark'),
    
    ## Comment - Create Read(detail 불필요) Update Delete
    path('<int:feed_pk>/comment/create/', views.comment_create, name='comment_create'),
    path('<int:feed_pk>/comment/<int:comment_pk>/update/', views.comment_update, name='comment_update'),
    path('<int:feed_pk>/comment/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
]