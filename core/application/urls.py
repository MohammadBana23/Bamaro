from django.urls import path
from .views import (
    SignUpView, LoginView , ProfileView , TravelView
)

app_name = 'accounts'

urlpatterns = [
    path('signup/' , SignUpView.as_view(), name='signup'),
    path('login/' , LoginView.as_view(), name='login'),
    # path('', ProfileView.as_view(), name='profile-authorized'),
    path('<slug:username>' , ProfileView.as_view(), name='profile'),
    path('travels/' , TravelView.as_view(), name='travels'),
]