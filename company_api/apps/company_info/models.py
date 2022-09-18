from django.db import models
import uuid

# Create your models here.


class Company(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField(max_length=255)
    company_ceo = models.CharField(max_length=255)
    company_address = models.CharField(max_length=512)
    inception_date = models.DateField()

    def __str__(self):
        return self.company_name

    def __str__(self):
        return self.company_name


class Team(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    team_lead_name = models.CharField(max_length=255)

    def __str__(self):
        return self.team_lead_name
