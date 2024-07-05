from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreateForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Password 확인", widget=forms.PasswordInput(), help_text="이전과 동일한 비밀번호를 입력하시오.")

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "name", "email", "birthday"]
        widgets = {
            "birthday":forms.DateInput(attrs={"type":"date"})
        }