from django import forms
from .models import Trainer, TrainingSession, Client

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['first_name', 'last_name', 'specialization', 'email', 'profile_image']

class TrainingSessionForm(forms.ModelForm):
    class Meta:
        model = TrainingSession
        fields = ['client', 'trainer', 'session_date']
        widgets = {
            'session_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        trainer = cleaned_data.get('trainer')
        session_date = cleaned_data.get('session_date')

        if trainer and session_date:
            session_time = session_date.time()
            session_weekday = session_date.weekday() # kade 0 e ponedelnik a 6 e nedela

            # proveruva dali denot spagja u rabotnite denovi na trenerot
            if not (trainer.work_days_start <= session_weekday <= trainer.work_days_end):
                raise forms.ValidationError(
                    f" The trainer {trainer.first_name} doesn't work this day of the week! Please choose another day."
                )

            # proverka na rabotno vreme (saati)
            if not (trainer.start_time <= session_time <= trainer.end_time):
                raise forms.ValidationError(
                    f"The trainer works from {trainer.start_time.strftime('%H:%M')} to {trainer.end_time.strftime('%H:%M')}! Please schedule the appointment within those times"     )

            # proverka na cel chas ili polovina cas
            if session_time.minute not in [0, 30]:
                raise forms.ValidationError("Appointments are available exclusively on the hour and half-hour (e.g., 9:00 AM, 9:30 AM, 10:00 AM).")

        return cleaned_data

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email']