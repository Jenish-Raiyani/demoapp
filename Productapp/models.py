from django.db import models

import datetime


def default_datetime():    
    now = datetime.datetime.now()   
    now.replace(microsecond=0)      
    return now

 
class Product(models.Model):
    name = models.CharField(max_length=50)
    weight = models.IntegerField()
    price= models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(db_index=True, default=default_datetime)
    updated_at = models.DateTimeField(db_index=True, null=False)


    def __str__(self):
        return self.name
 
