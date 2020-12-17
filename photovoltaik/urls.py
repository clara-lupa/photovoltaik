from django.urls import path, include
from rest_framework import routers
from yields import views

router = routers.DefaultRouter()
router.register(r'pv_yield', views.PvYieldViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

