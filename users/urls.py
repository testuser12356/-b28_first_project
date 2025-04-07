from django.urls import path

import users.views as views

profile = [
    path("user/profile", views.profile)
]

auth = [
    path("auth/login/", views.login_user),
    path("auth/logout/", views.logout_user),
    path("auth/register/", views.register_user)
]

urlpatterns = profile + auth
