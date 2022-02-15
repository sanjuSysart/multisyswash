from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.utils import timezone
import datetime
from PIL import Image
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):

        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):

        user = self.create_user(
            email,
            password=password,
            username=username,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True, )
    phone = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='userimages',null=True,blank=True)
    username = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email + "--" + self.username 

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


# Service Model

class ServiceDetails(models.Model):
    serviceId = models.AutoField( primary_key=True,unique=True)
    serviceName = models.CharField(max_length=255, blank=True)
    serviceCode = models.CharField(max_length=255, blank=True)
    serviceDate = models.DateField(default=datetime.date.today)
    user=models.ForeignKey(User,default=False,on_delete=models.CASCADE)
    trash = models.BooleanField(default=False)

# Cloth Model

class ClothDetails(models.Model):
    clothId = models.AutoField(primary_key=True, unique=True)
    clothName = models.CharField(max_length=255, blank=True)
    clothNameArabic = models.TextField(blank= True)
    clothCode = models.CharField(max_length=255, blank=True)
    clothDate = models.DateField(default=datetime.date.today)
    clothImg = models.ImageField(upload_to='images', blank=True, default='pic.jpg')
    posView = models.BooleanField(default = False)
    clothCount = models.IntegerField(default=0)
    user=models.ForeignKey(User,default=False,on_delete=models.CASCADE)
    trash = models.BooleanField(default=False)  

    def save(self, *args, **kwargs):
        super().save(*args, *kwargs)
        img = Image.open(self.clothImg.path)
        # img = resizeimage.resize_contain(img, [502, 502])
        nimg = img.convert('RGB')
        nimg.save(self.clothImg.path)



# Price Model

class PriceDetails(models.Model):
    priceId = models.AutoField(primary_key=True, unique=True)
    serviceName = models.CharField(max_length=255, blank=True)
    clothType = models.CharField(max_length=255, blank=True)
    price = models.IntegerField(blank=True)
    xprice = models.IntegerField(blank=True)
    user=models.ForeignKey(User,default=False,on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    trash = models.BooleanField(default=False)

# Account Model

class AccountDetails(models.Model):
    acTypeId = models.AutoField(primary_key=True, unique=True)
    acTypeName = models.CharField(max_length=255, blank=True)
    user=models.ForeignKey(User,default=False,on_delete=models.CASCADE)
    trash = models.BooleanField(default=False)





# Plant Model

class PlantDetails(models.Model):
    plantId = models.AutoField(primary_key= True, unique= True)
    plantName = models.TextField(max_length= 255, blank=True)
    location = models.CharField(max_length= 255, blank= True)
    clothType = models.CharField(max_length= 255, blank= True)
    contactName = models.CharField(max_length=255, blank=True)
    contactNumber = models.BigIntegerField(blank= True)
    user=models.ForeignKey(User,default=False,on_delete=models.CASCADE)
    trash = models.BooleanField(default= False)


