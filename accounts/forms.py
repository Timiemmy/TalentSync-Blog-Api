from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = UserCreationForm.Meta.fields + ('name',)


class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields
