from django.shortcuts import render
from . import forms

# Create your views here.

def regform(request):
    form = forms.Signup()
    if request.method == 'POST':
        form = forms.Signup(request.POST)
        html = 'we have recieved this form again'
        if form.is_valid():
            html = html + "The form is valid"
    else:
        html = 'Welcome for first time'
    return render(request, 'signup.html', {'html':html,'form':form})