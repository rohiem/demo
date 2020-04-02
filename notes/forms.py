from django import forms
from .models import Notes

class NoteForm(forms.ModelForm):

    class  Meta:
        model = Notes
        fields = ['title','content','tags']

