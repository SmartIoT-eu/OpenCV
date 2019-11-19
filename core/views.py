from django.shortcuts import render
from .models import Profile
# Create your views here.

def opencv(request):
    profiles = Profile.objects.all()
    return render(request,"core/core.html",{'profiles':profiles})