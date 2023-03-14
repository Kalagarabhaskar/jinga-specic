from django.shortcuts import render

# Create your views here.
def dhoni(request):
    d={'name':'boss'}
    return render(request,'sony.html',context=d)
