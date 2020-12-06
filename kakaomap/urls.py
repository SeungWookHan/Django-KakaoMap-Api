from django.conf.urls import url
from .views import ViewMap

urlpatterns = [
    url("view_map", ViewMap.as_view(), name="view_map"),
]