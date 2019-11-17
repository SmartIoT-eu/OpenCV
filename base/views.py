from django.shortcuts import render, HttpResponse
from .models import Profile

# Create your views here.
def index(request):
    profiles = Profile.objects.all()
    return render(request,"base/base.html",{'profiles':profiles})
