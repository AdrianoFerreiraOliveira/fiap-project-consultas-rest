from django.contrib import admin
from django.urls import path, include
from RestConsulta.views import MedicosViewSet, PacientesViewSet
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register("api-medicos", MedicosViewSet, basename="Medicos")
router.register("api-pacientes", PacientesViewSet, basename="Pacientes")

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="consultas_api",
        default_version="v1",
        description="Consulta de histórico de pacientes",
        terms_of_service="#",
        contact=openapi.Contact(email="hybridtheorytech@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("grappelli/", include("grappelli.urls")),
    path("controle/", admin.site.urls),
    path("", include(router.urls)),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
