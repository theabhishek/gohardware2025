from django.db import models
from datetime import datetime


# Create your models here.
class Contactmarble(models.Model):
    first_name = models.CharField(max_length=100)
   
    marble_id = models.IntegerField()
    customer_need = models.CharField(max_length=100)
    marble_title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
  
   
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    create_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email
