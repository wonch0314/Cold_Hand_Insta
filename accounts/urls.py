from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('<str:username>/follows/',views.js_follows,name='follows'),

    # path('profile/<str:username>/update/',views.update,name='update'),
    # path('profile/<str:username>/new_update/',views.new_update ,name='new_update'),
    path('profile/<str:username>/update/password/',views.password,name='password'),
    path('<str:username>/delete/', views.delete, name='delete'),
    path('profile/<str:username>/',views.profile,name='profile'),
    path('profile/<str:username>/update/',views.new_update ,name='update'),
    
    
    # path('profile/<str:username>/bk_feeds/',views.bookmark ,name='bk_feeds'),
    # path('profile/<str:username>/tag_feeds/',views.tag ,name='tag_feeds'),
    
    # path('new_profile/<str:username>/',views.new_profile,name='new_profile'),

    
]
