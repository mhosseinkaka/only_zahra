from django.urls import path
from poem_display.views import get_random_poem, get_poem_with_param

urlpatterns = [
    path('', get_random_poem, name='random_poem'),
    path('<int:poem_id>/', get_poem_with_param, name='poem_with_param'),
]
