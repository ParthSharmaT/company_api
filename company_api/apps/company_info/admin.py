from django.contrib import admin
from company_api.apps.company_info.models import Company,Team
# Register your models here.
admin.site.register([Company,Team])