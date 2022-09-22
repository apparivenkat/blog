from django.urls import path
from .views import about, add_post, contact, dashboard, delete_post, home, loginpage, logoutpage, signup, update_post

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('dashboard', dashboard, name='dashboard'),
    path('login', loginpage, name='login'),
    path('logout', logoutpage, name='logout'),
    path('signup', signup, name='signup'),
    path('addpost', add_post, name='addpost'),
    path('updatepost<int:id>', update_post, name='updatepost'),
    path('delete<int:id>', delete_post, name='delete')
]
