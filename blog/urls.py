# from .views import *
# from rest_framework.routers import DefaultRouter
# from django.urls import path, include
#
# router = DefaultRouter()
# router.register(r'employee', ProductsViews, basename='employee')
# urlpatterns = router.urls

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductsViews

router = DefaultRouter()
router.register(r'employee', ProductsViews, basename='employee')

urlpatterns = [
    path('', include(router.urls)),
]