from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Plot(models.Model):
    plot_number = models.CharField(max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Plot {self.plot_number}"
    
class UserAllotment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plots = models.ManyToManyField(Plot)



    


    
