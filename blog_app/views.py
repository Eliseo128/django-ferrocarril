from django.shortcuts import render

# Create your views here.
def ver_articulos(request):
    return render(request,'articulos.html')