from django import forms

class user_form(forms.Form):
    user_name = forms.CharField(required=True, label="Full Name", initial="Rony")
    user_email = forms.EmailField(label="User Email")
