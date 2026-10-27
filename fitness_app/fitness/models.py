from django.db import models
from datetime import time

# Create your models here.
class Trainer(models.Model):
    SPECIALTY_CHOICES = [
        ('strength', 'Strength & Conditioning'),
        ('hypertrophy', 'Muscle Hypertrophy'),
        ('weight_loss', 'Weight Loss & Fat Burn'),
        ('yoga', 'Yoga & Mobility'),
        ('pilates', 'Pilates'),
        ('rehab', 'Injury Rehabilitation'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(
        max_length=50,
        choices=SPECIALTY_CHOICES,
        default='strength'
    )
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(upload_to='trainers/', blank=True, null=True)

    # Rabotno vreme
    start_time = models.TimeField(default=time(8, 0))
    end_time = models.TimeField(default=time(20, 0))

    DAYS_OF_WEEK = [
        (0, 'Понеделник'),
        (1, 'Вторник'),
        (2, 'Среда'),
        (3, 'Четврток'),
        (4, 'Петок'),
        (5, 'Сабота'),
        (6, 'Недела'),
    ]
    work_days_start = models.IntegerField(choices=DAYS_OF_WEEK, default=0)  # Ponedelnik
    work_days_end = models.IntegerField(choices=DAYS_OF_WEEK, default=4)  # Petok

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_specialization_display()})"

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class TrainingSession(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    session_date = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Session: {self.client} with {self.trainer} on {self.session_date.strftime('%Y-%m-%d %H:%M')}"