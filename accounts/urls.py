# lines 2 - 8 added in template
from django.urls import path

from .views import CreateAccountView

urlpatterns = [
    path("create_account/", CreateAccountView.as_view(), name="create_account"),
]
