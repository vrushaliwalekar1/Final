from django.shortcuts import render

# Create your views here.
def add_new_student(request):
    return render(request, 'add_new_student.html')

def update_student(request):
    return render(request, 'update_student.html')

def list_all_student(request):
    return render(request, 'list_all_student.html')