from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image


class New(models.Model):
    user = models.ForeignKey(User, null='True', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='', blank='False', null='True')
    surname = models.CharField(max_length=50, default='', blank='False', null='True')
    role = models.CharField(max_length=50, default='', blank='False', null='True')
    number = models.CharField(max_length=50, default='', blank='False', null='True')
    date = models.DateTimeField(default=timezone.now, null='True')
    optional_number = models.CharField(max_length=50, default='', blank='False', null='True')
    address = models.CharField(max_length=50, default='', blank='False', null='True')
    reason = models.CharField(max_length=50, default='', blank='False', null='True')


def __str__(self):
    return self.name
    # ye sahi hai


class Status(models.Model):
    new = models.ForeignKey(New, null='true', on_delete=models.CASCADE)
    user = models.ForeignKey(User, null='True', on_delete=models.CASCADE)
    remark = models.CharField(max_length=50, default='')
    status = models.BooleanField(default='False')

    def __str__(self):
        return str(self.new)+" "+str(self.user)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}Profile'
    #overiding save method to resize img uploaded & we want to run save method of parent class thats why using super

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (250, 250)
            img.thumbnail(output_size)
            img.save(self.image.path)



# Create your models here.CASCADE means that if the user get deleted, delete the profile
# but if we delete the profile it wont delete the user it just a one way thing
