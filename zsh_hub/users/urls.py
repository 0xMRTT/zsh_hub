from django.urls import path

from zsh_hub.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
    user_settings_view,
)

from django.shortcuts import redirect

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path("settings/", view=user_settings_view, name="settings"),
]
