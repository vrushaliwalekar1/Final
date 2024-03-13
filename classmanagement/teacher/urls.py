from django.urls import path

from .views import add_new_teacher, update_teacher, list_all_teacher

urlpatterns = [
    path('', add_new_teacher),
    path('update_teacher/', update_teacher),
    path('list_all_teacher/', list_all_teacher),
]