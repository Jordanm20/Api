from django.contrib import admin
from django.urls import path, re_path
from apirest import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/sensores$', views.sensor_data_list),
    re_path(r'^api/sensores/(?P<pk>[0-9]+)$', views.sensor_data_detail),
    re_path(r'^api/lecturas$', views.lectura_data_list),
    re_path(r'^api/lecturas/(?P<pk>[0-9]+)$', views.lectura_data_detail),
    re_path(r'^db/nuevo-jwt', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r'^auth-jwt-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^auth-jwt-verify/', TokenVerifyView.as_view(), name='token_verify'),
]
