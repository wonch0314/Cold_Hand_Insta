from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('<str:username>/follows/',views.js_follows,name='follows'),

    path('profile/<str:username>/update/password/',views.password,name='password'),
    path('<str:username>/delete/', views.delete, name='delete'),
    path('profile/<str:username>/',views.profile,name='profile'),
    path('profile/<str:username>/update/',views.new_update ,name='update'),
]
