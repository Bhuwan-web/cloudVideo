"""cloudVideo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from users import urls as users_url
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("session-auth/", include("rest_framework.urls")),
    path(
        "swagger/",
        TemplateView.as_view(template_name="swagger.html", extra_context={"schema_url": "openapi-schema"}),
        name="swagger-ui",
    ),
    path(
        "openapi",
        get_schema_view(title="CloudApi", description="API for all things", version="1.0.0"),
        name="openapi-schema",
    ),
    path("api/users/", include(users_url)),
]