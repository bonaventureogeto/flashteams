from django.urls import path
from accounts.views import TeamCreateListAPIView


urlpatterns = [
    path('team', TeamCreateListAPIView.as_view(), name='create-team')
]
