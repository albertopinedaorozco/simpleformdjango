from django.shortcuts import render, redirect
from .forms import MeseroForm


def saludar(request):
    form = MeseroForm()
    return render(request,'saludo/index.html', { 'form': form })

def otraP(request):
    return render(request,'saludo/otrapagina.html')

def guardarMesero(request):
    print("En guardar mesero")
    if request.method=="POST":
        form = MeseroForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("otrapage")
        else:
            return redirect("otrapage")
    else:
        return render(request,'saludo/index.html', { 'form': form })


