from django.urls import path
from poem_display.views import get_random_poem

urlpatterns = [
    path('', get_random_poem, name='random_poem'),
]