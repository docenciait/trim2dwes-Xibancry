from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from django.contrib.auth import logout as auth_logout, login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def registro(request):
    template_data = {}
    
    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'usuarios/registro.html', {'template_data': template_data})
    
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            template_data['form'] = form
            return render(request, 'usuarios/registro.html', {'template_data': template_data})
    
def login(request):
    template_data = {}
    
    if request.method == 'GET':
        template_data['form'] = AuthenticationForm()
        return render(request, 'usuarios/login.html', {'template_data': template_data})
    
    elif request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            template_data['error'] = 'Usuario o contrasena incorrectos'
            return render(request, 'usuarios/login.html', {'template_data': template_data})
        else:
            auth_login(request, user)
            return redirect('lista_denuncias')
       
@login_required        
def logoutUser(request):
    if request.method == 'GET':
        auth_logout(request)

        return redirect('login')