from django.urls import path
from .views import SignUpView, Profile


urlpatterns = [
    # path('signup/', SignUpView.as_view(), name='signup'),
    path('<int:id>', Profile, name='profile' ),
]
