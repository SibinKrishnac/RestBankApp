from django.db import models


# Create your models here.
class Accounts(models.Model):
    accno=models.IntegerField(unique=True)
    username=models.CharField(max_length=120)
    balance=models.IntegerField(default=0)
    acnt_type=models.CharField(max_length=12)

    def __str__(self):
        return str(self.accno)

class Transactions(models.Model):
    accno=models.ForeignKey(Accounts,on_delete=models.CASCADE)
    r_acno=models.IntegerField()
    amount=models.IntegerField()
    date=models.DateField(auto_now=True)
    def __str__(self):
         return str(self.accno)