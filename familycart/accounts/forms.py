from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomCreateUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'phone_number',
                  'postal_code', 'town_name']


class CustomChangeUserForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'postal_code', 'town_name']
