from django.shortcuts import render

# Create your views here.
def first(request):
    d={'a':36,'b':24}
    return render(request,'one.html',d)

def second(request):
    d={'a':36,'b':24,'c':27}
    return render(request,'second.html',d)