from django.db import models
from patients.models import Patient
from django.contrib.auth.models import User

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True})
    date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Ожидается'), ('Done', 'Завершен')])

    def __str__(self):
        return f"{self.patient} - {self.doctor} at {self.date}"
