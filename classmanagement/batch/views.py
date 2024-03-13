from django.shortcuts import render

from .forms import CourseDetailsForm, BatchDetailsForm

# Create your views here.
def add_new_batch(request):
    form = BatchDetailsForm()
    if request.method == "POST":
        form = BatchDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success_response.html', {'data': 'Batch <value> added and will start from <value> date'})
        else:
            return render(request, 'invalid_response.html', {'error': form.error})
    return render(request, 'add_new_batch.html', {'form': form})

def add_new_course(request):
    form = CourseDetailsForm()
    if request.method == "POST":
        form = CourseDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success_response.html', {'data': 'Course <value> added'})
        else:
            return render(request, 'invalid_response.html', {'error': form.error})
    return render(request, 'add_new_course.html', {'form': form})

def list_all_batches(request):
    return render(request, 'list_all_batches.html')

def list_all_courses(request):
    return render(request, 'list_all_courses.html')