from django.urls import path 
from . import views
urlpatterns = [
    path('',views.home, name='homepage'),
    path('get/',views.get_cookie, name='get_cookies'),
    path('del/',views.delete_cookie, name='del_cookies'),
    path('set_s/',views.set_session, name='set_session'),
    path('get_s/',views.get_session, name='get_session'),
    path('del_s/',views.delete_session, name='del_session'),
]
