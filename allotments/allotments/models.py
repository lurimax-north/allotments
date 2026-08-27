from faker import Faker
from faker_animals import AnimalsProvider

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# Create your models here.


def validate_number_of_plots(obj):
    model = obj.__class__
    if model.objects.count() >= 18:
        raise ValidationError("You can only create 18 plots")

def make_anonymous_username():
    fake = Faker()
    fake.add_provider(AnimalsProvider)
    return f"{fake.safe_color_name()}-{fake.animal_name().split(" ")[-1]}".lower()


class Plot(models.Model):
    plot_number = models.PositiveSmallIntegerField(unique=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Plot {self.plot_number}"

    def clean(self):
        validate_number_of_plots(self)

    def occupied(self):
        return self.users.count() > 0
        
class User(AbstractUser):
    plot = models.ForeignKey(Plot, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')
    
    anonymous_username = models.CharField(max_length=100, default=make_anonymous_username)

    
