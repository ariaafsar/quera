from django.contrib.admin import ModelAdmin , register
from .models import Account

@register(Account)
class AccountAdmin(ModelAdmin):
    pass

# Register your models here.
