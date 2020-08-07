from django import forms

# from .models import Client
from .models import Coach_sessions, User_signup


class CoachSessionForm(forms.ModelForm):
    class Meta:
        model = Coach_sessions
        fields = [
            'session_details',
            'no_of_quiz',
            'hrs_of_quiz',
            'no_of_video',
            'hrs_of_video',
            'no_of_images',
            'hrs_of_images',
            'no_of_music',
            'hrs_of_music'
        ]


class UserSignupForm(forms.ModelForm):
    class Meta:
        model = User_signup
        fields = [
            'name',
            'email',
            'password',
            'password2',
            'country',
            'state',
        ]
