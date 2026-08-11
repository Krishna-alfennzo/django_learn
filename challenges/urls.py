from django.urls import path
from . import views

urlpatterns = [
    path("<str:month>", views.monthly_challenges),
    path("<int:month>", views.monthly_challenges_by_numbers)
]