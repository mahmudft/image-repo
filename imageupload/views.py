from django.contrib.auth import logout, authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse
# from django.views import View

from imageupload.forms import SignUpForm, LoginForm, UploadForm
from imageupload.models import Images
User = get_user_model()

def home(request):
    files = Images.objects.filter(security="public").all()
    return render(request, 'imageupload/home.html', {'data': files})

@login_required
def fileupload(request):
    upfiles = Images.objects.filter(author=request.user).all()
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            middleform = form.save(commit=False)
            middleform.author = request.user
            middleform.save()
            return redirect(reverse('home'))
        else:
            form = UploadForm()
    return render(request, 'imageupload/upload.html', {'form': form, "upfiles": upfiles})



def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'imageupload/signup.html', {'form': form})

def log_in(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        #end
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect(reverse('imagelist'))

    context = {'form': form}
    return render(request, 'imageupload/login.html', context)

def log_out(request):
    logout(request)
    return redirect('/')
