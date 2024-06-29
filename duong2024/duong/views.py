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

from django.core.paginator import Paginator
def street_list(request):
    streets = Street.objects.all()
    paginator = Paginator(streets, 15)  # Chia dữ liệu thành 15 tên đường mỗi trang
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'streets': streets,
        'page_obj': page_obj
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
    # return redirect(reverse_lazy('login'))
    return redirect(reverse_lazy('home'))

from tablib import Dataset
from .forms import UploadFileForm
from .resources import StreetResource
from django.http import HttpResponse

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            dataset = Dataset()
            new_streets = dataset.load(file.read(), format='xlsx')

            street_resource = StreetResource()
            result = street_resource.import_data(dataset, dry_run=True)  # Test the data import

            if not result.has_errors():
                street_resource.import_data(dataset, dry_run=False)  # Actually import now
                messages.success(request, 'Dữ liệu đã được import thành công.')
            else:
                messages.error(request, 'Đã có lỗi xảy ra trong quá trình import dữ liệu.')

            return redirect('upload_file')
    else:
        form = UploadFileForm()
    context = {
        'form': form
    }
    if request.user.is_authenticated:
        context['user_authenticated'] = True
    return render(request, 'streets/upload_file.html', context)

def export_streets_csv(request):
    street_resource = StreetResource()
    dataset = street_resource.export()

    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="streets.csv"'
    return response

def export_streets_xlsx(request):
    street_resource = StreetResource()
    dataset = street_resource.export()

    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="streets.xlsx"'
    return response