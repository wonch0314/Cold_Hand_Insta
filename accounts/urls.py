from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile/<str:username>/',views.profile,name='profile'),
    path('<str:username>/follows/',views.follows,name='follows'),
    path('profile/<str:username>/update/',views.update,name='update'),
    path('profile/<str:username>/update/password/',views.password,name='password'),
    path('profile/<str:username>/bk_feeds/',views.bookmark ,name='bk_feeds'),
    path('profile/<str:username>/tag_feeds/',views.tag ,name='tag_feeds'),
    
]
