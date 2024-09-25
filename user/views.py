from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.

#FBV
#CBV


@csrf_exempt
def test_view(request):

    if request.method == "GET":
        return HttpResponse('you are sending a get request')

    if request.method == "POST":
        return HttpResponse('you are sending a post request')


def home_page(request):
    context = {'welcome_title': 'welcome to our blog'}
    return render(request, 'HomePage.html', context)


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'register successful')
            return redirect('test')

        else:
            print(form.errors)
            messages.error(request, f'registeration failed you can see the erors.')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, "UserRegister.html", context)


def logout_custom(request):
    logout(request)
    return redirect('home_page')
