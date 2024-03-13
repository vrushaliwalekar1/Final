from django import forms

from .models import CourseDetails, BatchDetails

class CourseDetailsForm(forms.ModelForm):
    class Meta:
        model = CourseDetails
        fields = '__all__'

class BatchDetailsForm(forms.ModelForm):
    class Meta:
        model = BatchDetails
        fields = '__all__'