from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager, PermissionsMixin 

class AccountManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)
    
class Account(AbstractBaseUser, PermissionsMixin):
    accountID = models.CharField(max_length=100, primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, unique=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    accountRole = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['accountRole']

    objects = AccountManager()

    class Meta:
        db_table = "account"
    
    @property
    def is_anonymous(self):
        return False
    
    @property
    def is_authenticated(self):
        return True


class Vehicle(models.Model):
    vehicleID = models.CharField(max_length=100, primary_key=True,)
    vehicleName = models.CharField(max_length=100)
    vehicleModel = models.CharField(max_length=100)
    vehicleBrand = models.CharField(max_length=100)
    vehicleManufacturer = models.CharField(max_length=100)
    vehicleType = models.CharField(max_length=100)
    vehicleRentRate = models.FloatField()
    available = models.BooleanField(default=True)
    image = models.CharField(max_length=1000, default=None)

    class Meta:
        db_table = "vehicle"


class RentalAgreement(models.Model):
    rentID = models.CharField(max_length=100, primary_key=True)
    rentDate = models.DateField()
    numberOfDays = models.PositiveIntegerField()
    rentDue = models.FloatField(default= 0)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    class Meta:
        db_table = "rental_agreement"
