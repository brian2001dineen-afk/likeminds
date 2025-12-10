from django import forms
from allauth.account.forms import SignupForm

# Custom signup form
class CustomSignupForm(SignupForm):
    """
    Ensures that all form fields have the 'form-control' CSS class for Bootstrap styling.
    """
    # Loop through all fields and add 'form-control' class
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
    # Render form fields with custom placeholders and IDs
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'signupName', 'placeholder': 'Your name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'signupEmail', 'placeholder': 'Enter your email address'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'signupPassword', 'placeholder': 'Enter your password'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'signupConfirmPassword', 'placeholder': 'Enter your password again'})
    )

    # Ensure passwords match
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords do not match.")
        return cleaned_data
