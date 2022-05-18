from django.urls import path
from . import views

app_name = 'feeds'

urlpatterns = [
    path('', views.index, name='index'),
    ## Feed - Create Read(detail) Update Delete
    path('create/', views.create, name='create'),
    path('<int:feed_pk>/delete/', views.delete, name='delete'),
    path('<int:feed_pk>/like/', views.like, name='like'),
    path('<int:feed_pk>/bookmark/', views.bookmark, name='bookmark'),
    
    ## Comment - Create Read(detail 불필요) Update Delete
    path('<int:feed_pk>/comment/create/', views.comment_create, name='comment_create'),

    ## HashTag - search,, exist
    path('hashtag/search/<str:hash>/',views.hashtag_search, name='hashtah_search'),
    path('hashtag/exist/<str:hash>/',views.hashtag_exist, name='hashtah_exist'),

    ## UserTag - search, exist
    path('usertag/exist/<str:user>/',views.usertag_exist, name='usertag_exist'),
]
