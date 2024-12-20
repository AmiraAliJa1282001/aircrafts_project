# Generated by Django 4.2.16 on 2024-11-19 20:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("employee_id", models.CharField(max_length=10, unique=True)),
                (
                    "account_type",
                    models.CharField(
                        choices=[
                            ("Portfolio Controller", "Portfolio Controller"),
                            ("Project Controller", "Project Controller"),
                            ("Maintenance Executer", "Maintenance Executer"),
                            ("Shop Administrator", "Shop Administrator"),
                            ("Customer Representative", "Customer Representative"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "skill_specialty",
                    models.CharField(
                        choices=[
                            ("CS_B1", "CS_B1"),
                            ("CS_B2", "CS_B2"),
                            ("MECH", "MECH"),
                            ("STRUCTURE", "STRUCTURE"),
                            ("CLEANER", "CLEANER"),
                            ("PAINTER", "PAINTER"),
                            ("NDT", "NDT"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "authorizations",
                    models.TextField(
                        help_text="Comma-separated list of authorized aircraft types"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
