# Generated by Django 4.1.1 on 2022-09-16 11:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("company_name", models.CharField(max_length=255)),
                ("company_ceo", models.CharField(max_length=255)),
                ("company_address", models.CharField(max_length=512)),
                ("inception_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("team_lead_name", models.CharField(max_length=255)),
                ("company", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="company_info.company")),
            ],
        ),
    ]
