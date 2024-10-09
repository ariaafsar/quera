from django.urls import path
from .views import CreateClass

urlpatterns = [
    path('create/', CreateClass.as_view(), name='create_class'),
]