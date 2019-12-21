from django.db import models
from core.models import TimestampedModel

class Expense(TimestampedModel):
    currency = models.fields.CharField(max_length=5)
    ammount = models.fields.DecimalField(max_digits=10, decimal_places=2)
    

class RecurringExpense(Expense):
    start_date = models.fields.DateField()
    end_date = models.fields.DateField(null=True, blank=True)
