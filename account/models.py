from django.db import models
import uuid
from userauths.models import User
from shortuuid.django_fields import ShortUUIDField
#from shortuuidfield import ShortUUIDField
#from shortuuidfield import ShortUUIDField
# Create your models here.

ACCOUNT_STATUS = (
    ("active", "Active"),
    ("pending", "Pending"),
    ("in-active", "In-active")
)

MARITAL_STATUS = (
    ("married", "Married"),
    ("single", "Single"),
    ("other", "Other")
)

GENDER = (
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other")
)


IDENTITY_TYPE = (
    ("national_id_card", "National ID Card"),
    ("drivers_licence", "Drives Licence"),
    ("international_passport", "International Passport")
)


def user_directory_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s_%s" % (instance.id, ext)
    return "user_{0}/{1}".format(instance.user.id, filename)



class Account(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    account_number = ShortUUIDField(length=10, unique=True,max_length= 25, prefix="217", alphabet="1234567890" )
    account_id = ShortUUIDField(length=7, unique=True,max_length= 25, prefix="DEX", alphabet="1234567890" )
    pin_number = ShortUUIDField(length=4, unique=True,max_length= 7 , alphabet="1234567890" )
    red_code = ShortUUIDField(length=10, unique=True,max_length= 20, prefix="217", alphabet="abcdefghi1234567890" )
    account_status = models.CharField(max_length=100, choices= ACCOUNT_STATUS, default="in-active")
    date = models.DateTimeField(auto_now_add=True)
    kyc_submitted = models.BooleanField(default=False)
    kyc_confirmed = models.BooleanField(default=False)
    recommended_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="recommended_by")

    class Meta:
        ordering = ['-date']


    def __str__(self):
        return f"self.user"
       