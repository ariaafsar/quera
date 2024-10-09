from django.urls import path
from .views import CreateClass

urlpatterns = [
    path('create_class/', CreateClass.as_view(), name='create_class'),
]