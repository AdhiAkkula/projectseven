from django.shortcuts import render

# Create your views here.
def third(request):
    d={'a':36,'b':24,'c':27}
    return render(request,'third.html',d)

def forth(request):
    d={'name':'Adhi'}
    return render(request,'forth.html',d)