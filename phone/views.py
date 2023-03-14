from django.shortcuts import render

# Create your views here.
def hardhik(request):
    d={'age':'22'}
    return render(request,'sony1.html',context=d)

