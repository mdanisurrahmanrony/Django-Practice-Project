from django.shortcuts import render
from django.http import HttpResponse
from django_practice_app.models import Musician, Album
from django_practice_app import forms

# Create your views here.

def index(request):
    # SELECT * FROM Musician ORDER BY first_name
    musician_list = Musician.objects.order_by('first_name')
    diction = {'text_1':'This is a list of Musician', 'musician': musician_list}
    return render(request, 'django_practice_app/index.html', context=diction)

def form(request):
    new_form = forms.user_form()
    if request.method == 'POST':
        new_form = forms.user_form(request.POST)

        if new_form.is_valid():
            diction.update({'field':new_form.cleaned_data['field']})
            diction.update({'form_submitted':"Yes"})

    diction = {'test_form' : new_form, 'heading_1' : "This form is created using django library"}
    return render(request, 'django_practice_app/form.html', context=diction)
