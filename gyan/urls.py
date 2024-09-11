from django.urls import path
from gyan import views 
from django.contrib.auth import views as auth_views


urlpatterns = [
     path("", views.signup, name="signup"),
      path("home/", views.home, name="home"),
     path("about/", views.about, name="about"),
     path("contract/", views.contract, name="contact"),
     path("base/", views.base, name="base"),
     path("login/", views.user_login, name="user_login"),
     path("logout/", views.user_logout, name="user_logout"),
    #  path("forget/", views.forget_password, name="forget_password"),
    #  path('reset/',views.password_reset_confirm, name='password_reset_confirm'),
    #  path("password_reset_done'/", views.password_reset_done, name="password_reset_done"),
    #path("change/", views.change_password, name="change")
     
     

    
  
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path("change-password/", auth_views.PasswordChangeView.as_view(template_name='change_password.html'),name='change_password'),
    path("password_change_done/", auth_views.PasswordChangeView.as_view(template_name='password_change_done.html'),name='password_change_done'),
    #  path('profile/<int:user_id>/', views.user_profile, name='user_profile'),
    

   
    
    
]