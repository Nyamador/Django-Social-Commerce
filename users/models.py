from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import VelocityUserManager

#Recommended by documentation for future User model customizations
class VelocityUser(AbstractUser):
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=10,blank=True)
    fullname = models.CharField(max_length=50,blank=True)
    is_influencer = models.BooleanField(_('influencer'), default=False)
    is_seller = models.BooleanField(_('seller'),default=False)

    USERNAME_FIELD = 'email'

    objects = VelocityUserManager()#custom user Manager to Replace username identifier with email

    REQUIRED_FIELDS = []


    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        split_fullname = self.fullname.split(" ")
        firstname = split_fullname[0]
        lastname = split_fullname[-1]
        new_fullname = f'{firstname} {lastname}'
        return new_fullname


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="")
    business_name = models.CharField("Business Name", max_length=100 ,default="")
    business_email = models.EmailField("Business Email", blank=True,default="")
    business_registration_number = models.CharField("Regsitration Number", max_length=50, default="")
    shop_name = models.CharField("Shop Name", max_length=50, default="")
    tax_id = models.CharField("Tax Identification Number", max_length=100, default="")
    country = models.CharField("Country", max_length=100)
    region = models.CharField("State/Region/Province")
    city = models.CharField("City", max_length=100)
    bank_name = models.CharField("Bank", max_length=100)
    account_number = models.CharField("Account Number", max_length=30,blank=True)
    account_holder = models.CharField("Account Holder's Name", max_length=100,blank=True)
    momo_number = models.CharField("Mobile Money Number", max_length=10, null=True, blank=True)

    def __str__(self):
        return self.user
