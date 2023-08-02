from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.SignInView.as_view(), name='signin'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signout/', views.SignOutView.as_view(), name='signout'),
    path('activate/<uidb64>/<token>', views.activate,
         name='activate'),  # url for account activation
    path('change_password/', views.MyPasswordChangeView.as_view(),
         name='change_password'),
    path('reset_password/', views.MyPasswordResetView.as_view(),
         name='reset_password'),
    path('reset_password_done/', views.MyPasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.MyPasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path('reset_password_complete/', views.MyPasswordResetCompleteView.as_view(),
         name="password_reset_complete"),


]
