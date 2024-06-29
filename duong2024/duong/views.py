from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Street
from .forms import StreetForm
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy

def home(request):
    streets = Street.objects.all()

    context = {
        'streets': streets
    }
    if request.user.is_authenticated:
        context['user_authenticated'] = True
    return render(request, 'streets/home.html', context)

def street_list(request):
    streets = Street.objects.all()
    context = {
        'streets': streets
    }
    if request.user.is_authenticated:
        context['user_authenticated'] = True
    return render(request, 'streets/street_list.html', context)

def street_detail(request, pk):
    street = get_object_or_404(Street, pk=pk)
    context = {
        'street': street
    }
    if request.user.is_authenticated:
        context['user_authenticated'] = True
    return render(request, 'streets/street_detail.html', context)

# @login_required
def add_street(request):
    if request.method == 'POST':
        form = StreetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('street_list')
    else:
        form = StreetForm()
    context = {
        'form': form
    }
    if request.user.is_authenticated:
        context['user_authenticated'] = True
    return render(request, 'streets/add_street.html', context)

@login_required
def edit_street(request, pk):
    street = Street.objects.get(pk=pk)
    if request.method == 'POST':
        form = StreetForm(request.POST, instance=street)
        if form.is_valid():
            form.save()
            return redirect('street_list')
    else:
        form = StreetForm(instance=street)
    context = {
        'form': form
    }
    if request.user.is_authenticated:
        context['user_authenticated'] = True
    return render(request, 'streets/edit_street.html', context)

@login_required
def delete_street(request, pk):
    street = Street.objects.get(pk=pk)
    street.delete()
    return redirect('home')

# @login_required
def search_street(request):
    if request.method == 'GET':
        search_query = request.GET.get('search', '')

        if search_query:
            streets = Street.objects.filter(name__icontains=search_query)
        else:
            streets = Street.objects.all()
        context = {
            'streets': streets,
            'search_query': search_query
        }
        if request.user.is_authenticated:
            context['user_authenticated'] = True
        return render(request, 'streets/search_results.html', context)

    else:
        return redirect('home')


def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('home'))

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse_lazy('home'))
        else:
            messages.error(request, 'Tài khoản hoặc mật khẩu không đúng.')

    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('login'))