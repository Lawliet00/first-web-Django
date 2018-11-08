from django.shortcuts import render
from django.http import HttpResponse

def Index(request):
	return render(request, 'web/index.html')

def Criterio_Estimado(request):
	return render(request, 'web/criterios-estimados.html')

def Max_verosimilitud(request):
	return render(request, 'web/max-verosimilitud.html')

def Min_cuadrados(request):
	return render(request, 'web/min-cuadrados.html')

def Ley_correlacion(request):
	return render(request, 'web/ley-de-correlacion.html')

def Intervalo(request):
	return render(request, 'web/intervalo-de-confianza.html')

def Dist_T_Student(request):
	return render(request, 'web/distribucion-t-student.html')

def Dist_Chi_cuadrados(request):
	return render(request, 'web/distribucion-chi-cuadrados.html')

def Prueba_hipotesis(request):
	return render(request, 'web/prueba_hipotesis/prueba_hipotesis.html')

def form_general(request):
	return render(request, 'web/prueba_hipotesis/formulacion-general.html')

def Dist_normal(request):
	return render(request, 'web/prueba_hipotesis/distribucion-normal-de-varianza-conocida.html')

def Prueba_bondad(request):
	return render(request, 'web/prueba_hipotesis/prueba-de-bondad-de-ajuste.html')

def Validación(request):
	return render(request, 'web/prueba_hipotesis/validacion-de-modelos.html')
