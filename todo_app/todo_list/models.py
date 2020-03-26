from django.db import models

# Create your models here.

class List(models.Model):
    item = models.CharField(max_length = 200)  #Text of length 200 
    completed = models.BooleanField(default = False)  #When we add an item it will automatically label as not completed 
   

    def __str__(self): #important for the admin to show data as the datatypes we want listed 
        return self.item + ' | ' +  str(self.completed)