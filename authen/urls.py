from django.urls import path
from authen import views


urlpatterns = [
    path('signup/',views.handel_signup,name="signup"),
    path('login/',views.handel_login,name="login"),
    path('logout/',views.handel_logout,name="logout"),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),
]
