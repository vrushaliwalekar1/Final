from django.urls import path

from .views import add_new_student, update_student, list_all_student

urlpatterns = [
    path('', add_new_student),
    path('update_student/', update_student),
    path('list_all_student/', list_all_student),
]