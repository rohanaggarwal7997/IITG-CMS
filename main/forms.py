from django import forms
from .models import *


class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['title', 'date', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker'})
        }

class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievements
        fields={'title','date','description'}
        widgets={
            'date': forms.DateInput(attrs={'class': 'datepicker'})
        }

class NForm(forms.ModelForm):
    class Meta:
        model = News
        fields={'date','description'}
        widgets={
            'date': forms.DateInput(attrs={'class': 'datepicker'})
        }

class ddeskForm(forms.ModelForm):
    class Meta:
        model=ddesk
        fields={'description'}

class IForm(forms.ModelForm):
    class Meta:
        model = initiatives
        fields={'description'}
