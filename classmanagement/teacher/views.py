from django.shortcuts import render

# Create your views here.
def add_new_teacher(request):
    return render(request, 'add_new_teacher.html')

def update_teacher(request):
    return render(request, 'update_teacher.html')

def list_all_teacher(request):
    return render(request, 'list_all_teacher.html')

