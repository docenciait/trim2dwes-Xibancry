from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Denuncia
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class lista_denuncias(LoginRequiredMixin, ListView):
    model = Denuncia
    template_name = 'lista_denuncias.html'

class crear_denuncia(LoginRequiredMixin, CreateView):
    model = Denuncia
    template_name = 'crear_denuncia.html'
    fields = '__all__'
    success_url = reverse_lazy('lista_denuncias')

class editar_denuncia(LoginRequiredMixin, UpdateView):
    model = Denuncia
    template_name = 'editar_denuncia.html'
    fields = '__all__'
 
class eliminar_denuncia(LoginRequiredMixin, DeleteView):
    model = Denuncia
    template_name = 'eliminar_denuncia.html'