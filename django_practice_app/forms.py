from django import forms

class user_form(forms.Form):
    #boolean_field = forms.BooleanField(required=False)
    #field = forms.CharField(max_length=15, min_length=5)
    #choices = (('','---SELECT OPTION--'),('1','First'),('2','Second'),('3','Third'))
    #field = forms.ChoiceField(choices=choices, required=False)
    #choices = (('A','A'),('B','B'),('C','C'))
    #field = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)
    #choices = (('','---SELECT OPTION--'),('1','First'),('2','Second'),('3','Third'))
    #field = forms.MultipleChoiceField(choices=choices, required=False)
    choices = (('A','A'),('B','B'),('C','C'))
    field = forms.MultipleChoiceField(choices=choices, widget=forms.CheckboxSelectMultiple)
