from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
import uuid

# Create your models here.



class AccountManager(BaseUserManager):
    def create_user(self, email, name, address, bdate, pnumber, password=None):
        if not email:
            raise ValueError("Email address required.")
        if not name:
            raise ValueError("Name required.")
        if not address:
            raise ValueError("Address required.")
        if not bdate:
            raise ValueError("Birthdate required.")
        if not pnumber:
            raise ValueError("Phone number required.")
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            address=address,
            bdate=bdate,
            pnumber=pnumber,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, name, address, bdate, pnumber, password):
        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            password=password,
            address=address,
            bdate=bdate,
            pnumber=pnumber,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user 

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    name = models.CharField(verbose_name="name", max_length=70)
    address = models.CharField(verbose_name="address", max_length=200)
    bdate = models.DateField(verbose_name="Birthdate")
    pnumber = PhoneNumberField(null=True)
    date_joined	= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'address', 'bdate', 'pnumber']

    objects = AccountManager()

    def __str__(self):
        return str(self.name)

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True 
    


class Product(models.Model):
    pro_email = models.ForeignKey(Account, on_delete=models.CASCADE,default="")
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False ,unique=True)
    product_image = models.ImageField(upload_to='product_images')
    product_name = models.CharField(verbose_name="product_name", max_length=70)
    product_price = models.IntegerField(verbose_name="product_price")
    product_description = models.CharField(verbose_name="product_deascription", max_length=500)
    product_category = models.CharField(verbose_name="product_category", max_length=70)
    product_location = models.CharField(verbose_name="product_location", max_length=500)
    


    def __str__(self):
        return str(self.product_name)



