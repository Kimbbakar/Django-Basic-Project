from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.


def signup(request):
    form = SignUpForm()
    return render(request, 'signup.html',{'form':form } )