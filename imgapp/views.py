from django.shortcuts import render

# Create your views here.
def img(request):
    return render(request,'profile.html',{'img':img})

