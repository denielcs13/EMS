from django.conf.urls import url

from . import views

app_name ='Login'

urlpatterns = [
    # /home/
    url(r'^$', views.home, name='home_page'),

    # checking for login/
    url(r'^checklogin/', views.check_login),

    # /home/user_logout/
    url(r'^user_logout/', views.user_logout,name='logout'),

    # /home/view_profile
    url(r'^view_profile/',views.viewprofile, name='viewprofile'),

    # /home/changepassword/
    url(r'^changepassword/',views.changepassword,name='changepassword'),

    # /home/savechangepassword/
    url(r'^savechangepassword', views.savechangepassword, name='savechangepassword'),

    # /home/save/
    url(r'^saveprofile/', views.saveprofile, name='saveprofile')
]
