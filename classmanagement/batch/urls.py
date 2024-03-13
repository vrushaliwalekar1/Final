from django.urls import path

from .views import add_new_batch, add_new_course, list_all_batches, list_all_courses

urlpatterns = [
    path('add_new_batch/', add_new_batch),
    path('add_new_course/', add_new_course),
    path('list_all_batches/', list_all_batches),
    path('list_all_courses/', list_all_courses)
]