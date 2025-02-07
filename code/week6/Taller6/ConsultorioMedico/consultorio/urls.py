from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from consultorio import views

app_name = 'consultorio'
urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('pacientes', TemplateView.as_view(template_name="pacientes.html"), name="pacientes"),
    path('medicos', TemplateView.as_view(template_name="medicos.html"), name="medicos"),
    path('especialidades', TemplateView.as_view(template_name="especialidades.html"), name="especialidades"),
    path('citas', views.numero_de_citas, name="numero_citas"),
]