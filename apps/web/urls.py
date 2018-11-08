from django.urls import path, include
from apps.web.views import Index, Max_verosimilitud, Min_cuadrados, Ley_correlacion, \
	 Intervalo, Dist_T_Student, Dist_Chi_cuadrados, Prueba_hipotesis, form_general, \
	 Dist_normal, Prueba_bondad, Validación, Criterio_Estimado

urlpatterns = [
    path('', Index),
    path('criterios-estimados', Criterio_Estimado),
    path('max-verosimilitud', Max_verosimilitud),
    path('min-cuadrados', Min_cuadrados),
    path('ley-de-correlacion', Ley_correlacion),
	path('intervalo-de-confianza', Intervalo),
	path('distribucion-t-student', Dist_T_Student),
	path('distribucion-chi-cuadrados', Dist_Chi_cuadrados),
	path('prueba-hipotesis', Prueba_hipotesis),
	path('prueba-hipotesis/formulacion-general', form_general),
	path('prueba-hipotesis/distribucion-normal-de-varianza-conocida', Dist_normal),
	path('prueba-hipotesis/prueba-de-bondad-de-ajuste', Prueba_bondad),
	path('prueba-hipotesis/validacion-de-modelos', Validación),
]
