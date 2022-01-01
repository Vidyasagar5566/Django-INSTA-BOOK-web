from django.db import models

# Create your models here.

class user_uploads(models.Model):
    u_name = models.CharField(max_length = 100)
    U_profile_pic = models.ImageField(upload_to = 'pics')
    U_main_pic = models.ImageField(upload_to = 'pics')
    caption = models.TextField()
    comments = models.TextField(default="")



