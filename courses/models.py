from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255)
    course_location = models.CharField(max_length=255)
    tee_time = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    confirmation_code = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.user.username} - {self.course_name} at {self.tee_time}"

