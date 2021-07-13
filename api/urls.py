from django.urls import path, re_path
from django.conf.urls import url
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = "api"

schema_view = get_schema_view(
    openapi.Info(
        title="Session Auth Api",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.sessionauth.com/policies/terms/",
        contact=openapi.Contact(email="azaz.hassan@techno-soft.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    url(
        "^$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"
    ),
]
