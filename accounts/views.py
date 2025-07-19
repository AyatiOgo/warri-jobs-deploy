from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import RegularUserCreationForm, RegularUSerLoginForm
from django.contrib.auth import login, logout, authenticate
from jobs.models import JobsModel
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from jobBoard.settings import DEFUALT_FROM_EMAIL


# Create your views here.

def userRegistrationView(request):
    if request.method == 'POST':
        form = RegularUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            plain_message = f'Hello {user.full_name} welcome to Warri Jobs '
            html_messgae = render_to_string('email-template.html', {'user':user})
            email = EmailMessage(
                subject='Welcome to Warri Jobs',
                body=html_messgae,
                from_email=DEFUALT_FROM_EMAIL,
                to=[user.email],
            )
            email.content_subtype = "plain"  # just to be safe
            email.send(fail_silently=False)
            return redirect('home')
    else: 
        form = RegularUserCreationForm()
    context = {'form' : form}
    return render(request, 'register.html', context)


def userLoginView(request):
    if request.method == 'POST':
        form = RegularUSerLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = RegularUSerLoginForm()
    return render(request, "login.html", {'form':form})

def userLogoutView(request):
    logout(request)
    return redirect('login')

@login_required
def add_saved(request, id):
    job = JobsModel.objects.get(id=id)
    if job.saved.filter(id=request.user.id).exists():
        job.saved.remove(request.user)
    else :
        job.saved.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def saved_jobs(request):
    jobs = JobsModel.objects.filter(saved=request.user)
    return render(request, 'saved-jobs.html', {"jobs":jobs} )