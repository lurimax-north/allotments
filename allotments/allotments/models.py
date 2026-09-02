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
    anonymous_user = models.BooleanField(default=False)
    def __str__(self):
        if self.anonymous_user:
            return self.anonymous_username
        return f"{self.first_name} {self.last_name}"

class Message(models.Model):
    message = models.TextField()
    title = models.CharField(max_length=100, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"Message {self.pk} by {self.created_by.username}"
    class Meta:
        ordering = ['-created_at', "-id"]

class Comment(models.Model):
    comment = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created_at', '-id']

    def __str__(self):
        return f"Comment {self.pk} by {self.created_by.username} for message {self.message.pk}"