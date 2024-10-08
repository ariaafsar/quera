from django.contrib.admin import register , ModelAdmin
from .models import Class

@register(Class)
class ClassAdmin(ModelAdmin):
    pass
# Register your models here.
