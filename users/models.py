from django.contrib.auth.models import User
from django.db import models
#PC12345@@!!
class UserProfile(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ('Portfolio Controller', 'Portfolio Controller'),
        ('Project Controller', 'Project Controller'),
        ('Maintenance Executer', 'Maintenance Executer'),
        ('Shop Administrator', 'Shop Administrator'),
        ('Customer Representative', 'Customer Representative'),
    ]

    SKILL_CHOICES = [
        ('CS_B1', 'CS_B1'),
        ('CS_B2', 'CS_B2'),
        ('MECH', 'MECH'),
        ('STRUCTURE', 'STRUCTURE'),
        ('CLEANER', 'CLEANER'),
        ('PAINTER', 'PAINTER'),
        ('NDT', 'NDT'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    employee_id = models.CharField(max_length=10, unique=True)
    account_type = models.CharField(max_length=30, choices=ACCOUNT_TYPE_CHOICES)
    skill_specialty = models.CharField(max_length=30, choices=SKILL_CHOICES)
    authorizations = models.TextField(help_text="Comma-separated list of authorized aircraft types")

    def __str__(self):
        return f"{self.user.username} - {self.account_type}"
