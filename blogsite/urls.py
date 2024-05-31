from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include
from django.contrib import admin

schema_view = get_schema_view(
    openapi.Info(
        title="Employee",
        default_version='v 1.0.0',
        description="Xodimlar malumotlari",
        terms_of_service="https:/www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@gamil.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('blog.urls')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='sechema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='sechema-redoc'),
]



# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/', include('blog.urls')),
# ]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
