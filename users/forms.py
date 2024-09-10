from django import forms
from django.contrib.auth.models import User
from .models import Profile

class ProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=150)

    class Meta:
        model = Profile
        fields = ['username', 'bio', 'avatar']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].initial = self.instance.user.username

    def save(self, commit=True):
        user = self.instance.user
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
        return super(ProfileForm, self).save(commit)
