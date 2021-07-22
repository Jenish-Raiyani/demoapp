from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()


from django.contrib.auth.models import User
import datetime


def default_datetime():    
    now = datetime.datetime.now()   
    now.replace(microsecond=0)      
    return now


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    created_at = models.DateTimeField(db_index=True, default=default_datetime)
    updated_at = models.DateTimeField(db_index=True, null=False)

    
     