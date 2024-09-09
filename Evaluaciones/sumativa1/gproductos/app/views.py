from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def resultado(request):
    return render(request, 'productos/resultado.html')
def registro(request):
    return render(request, 'productos/registro.html')
def consulta(request):
    return render(request, 'productos/consulta.html')


