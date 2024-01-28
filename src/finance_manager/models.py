from django.conf import settings
from django.db import models
from django.utils.timezone import now


class Account(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.IntegerField()

    CURRENCY_CHOICES = [
        ("USD", "US Dollars"),
        ("EUR", "Euro"),
        ("BYN", "Belarusian rubles"),
    ]
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default="BYN")

    def __str__(self) -> str:
        return f"{self.user}"


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"


class Transaction(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=1000, null=True, blank=True)
    amount = models.IntegerField()
    date = models.DateTimeField(default=now)
    is_income = models.BooleanField(default=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        action = "spent"
        if self.is_income:
            action = "received"
        return f"{self.title}\n{self.amount / 100} {self.account.currency} {action}"

    def save(self, *args, **kwargs):
        if self.is_income:
            self.account.balance += self.amount
        else:
            self.account.balance -= self.amount
        self.account.save()
        super(Transaction, self).save(*args, **kwargs)
