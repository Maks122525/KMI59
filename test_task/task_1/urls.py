from django.urls import path
from rest_framework.routers import SimpleRouter

from.views import *

router = SimpleRouter()
router.register(r'^api/data', DataView, basename='data_all')

urlpatterns = [
    path('', index, name="index"),
]
urlpatterns += router.urls
