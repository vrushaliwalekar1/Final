from django.db import models

# Create your models here.
courses = (
    ("python", "Python"),
    ("java", "Java")
)

class CourseDetails(models.Model):
    course_name = models.CharField(
        max_length=25,
        choices = courses,
        default = "python"
    )
    duration = models.IntegerField(verbose_name= "Duration In Months")
    fees = models.IntegerField(verbose_name="Fees In RS.")

class BatchDetails(models.Model):
    batch_name = models.CharField(max_length=25)
    start_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=False)
    course = models.ForeignKey(CourseDetails, on_delete=models.SET_NULL, blank=True, null=True)