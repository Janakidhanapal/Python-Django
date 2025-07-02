from django.urls import path
from .views import *

urlpatterns = [
    path('student_entry/', student_entry, name='student_entry'),
    path('process_student_entry/', process_student_entry, name='process_student_entry'),
    path('display_stud_detail/', display_stud_detail, name='display_stud_detail')
]
