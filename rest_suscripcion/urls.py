from django.urls import path
from rest_suscripcion.views import obtener_suscripcion, activar_suscripcion, eliminar_suscripcion

urlpatterns = [
    path('obtener_suscripcion', obtener_suscripcion, name="obtener_suscripcion"),
    path('activar_suscripcion', activar_suscripcion, name="activar_suscripcion"),
    path('eliminar_suscripcion', eliminar_suscripcion, name="eliminar_suscripcion"),
]