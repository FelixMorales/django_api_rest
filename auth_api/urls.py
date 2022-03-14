from django.urls import path

from auth_api.views.auth_views import LoginView, LogoutView


urlpatterns = [
    path('login', LoginView.as_view(), name='Auth'),
    path('logout', LogoutView.as_view(), name='logout')
]