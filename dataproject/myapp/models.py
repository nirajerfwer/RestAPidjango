from django.db import models

class Data(models.Model):
          first_name = models.CharField(max_length=20)  
          last_name  = models.CharField(max_length=30)  
          contact    = models.IntegerField()
          dob        = models.DateField()  
          email      = models.EmailField(max_length=50)  
          age        = models.IntegerField() 
