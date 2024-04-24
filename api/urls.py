from django.urls import path
from api.views import SearchAPIView


urlpatterns = [
    path("", SearchAPIView.as_view())
]