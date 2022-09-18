from django.contrib import admin
from django.urls import path
from company_api.apps.company_info.api.views import CompanyView, TeamView, CompanyDetailView


app_name = "company_info"
urlpatterns = [
    path("company/", CompanyView.as_view(), name="company"),
    path("team/", TeamView.as_view(), name="team"),
    path("team/?id=<str:id>", TeamView.as_view(), name="create_team"),
    path("company_detail/", CompanyDetailView.as_view(), name="company_name_detail"),
    path("company_detail/?company_id=<str:company_id>", CompanyDetailView.as_view(), name="company_detail"),
]
