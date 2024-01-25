from django.db import models


class ihaalls(models.Model):
    Id = models.AutoField(primary_key=True)
    ihaName = models.CharField(max_length=50)
    serialNo = models.CharField(max_length=50)
    yearOfProduction = models.DateField()
    numbers = models.IntegerField()
    monthOfee = models.FloatField()
    currency = models.CharField(max_length=40, default="TL")
    rentalActive = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        self.isDeleted = True

        self.save()

    def save(self, *args, **kwargs):
        if self.numbers == 0:
            self.rentalActive = False
        else:
            self.rentalActive = True
        super().save(*args, **kwargs)


class ihainformation(models.Model):
    Id = models.AutoField(primary_key=True)
    rentihaid = models.ForeignKey(
        ihaalls, on_delete=models.SET_NULL,limit_choices_to={"rentalActive": True,"isDeleted":False}, null=True
    )
    rentmonth = models.IntegerField()
    rentcurrency = models.CharField(max_length=50)
    item = models.IntegerField(default=0)
    amount = models.FloatField(default=0)
    currency = models.CharField(max_length=40, default="TL")
    rentalPeriodOver = models.BooleanField(default=False)

class UserLogin(models.Model):
    Id = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    Admin=models.BooleanField(default=0)
