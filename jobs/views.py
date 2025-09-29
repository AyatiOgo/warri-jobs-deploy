from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import JobForm
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

def homeview(request):
    query = request.GET.get('search')
    if query:
        jobs = JobsModel.objects.filter( Q(title__icontains=query) | Q(categories__contains=query) )
        return redirect(f'search/?search={query}')
    else:
        jobs = JobsModel.objects.all().order_by('-date_posted')
    categories = JobsModel.CATEGORY_CHOICES
    user = request.user
    context = {
        'jobs':jobs,    
        'categories' : categories,
        'query' : query,
        'user' : user,
    }
    return render(request, "index.html", context)

def jobDetailView(request, slug):
    job = JobsModel.objects.get(slug=slug)
    context = {
        'job' : job
    }
    return render(request, "job-detail.html", context)

def searchView(request):
    query = request.GET.get('search', '').strip()
    job_type_search = request.GET.get('job-type', '').strip()
    jobs = JobsModel.objects.all().order_by('-date_posted')
    # filters
    if query:
        jobs = JobsModel.objects.filter( Q(title__icontains=query) | Q(categories__contains=query) | Q(description__icontains=query) )
    if job_type_search :
        jobs = JobsModel.objects.filter(job_type__icontains=job_type_search)

    job_type_j = JobsModel.JOB_TYPE_CHOICES
    work_location = JobsModel.WORK_LOCATION_CHOICES
    categories = JobsModel.CATEGORY_CHOICES

    # p = Paginator(jobs, 2)
    # page = request.POST.get('page')
    # job_pages = p.get_page(page)

    context = {
        'query':query,
        'job_type':job_type_j,
        'work_location':work_location,
        'categories' : categories,

        # 'job_type_search' : job_type_search
    }
    return render(request, "search.html", context )

def joblist(request):
    query = request.POST.get('search', '').strip()
    job_type = request.POST.get('job-type', 'all').strip()
    work_location = request.POST.get('work_location', 'all').strip()

    jobs = JobsModel.objects.all()

    if query:
        jobs = jobs.filter( Q(title__icontains=query) | Q(categories__contains=query) | Q(description__icontains=query) )


    if job_type != 'all':
        jobs = jobs.filter(job_type__icontains=job_type)

    if work_location != 'all':
        jobs = jobs.filter(work_location__icontains=work_location)

    p = Paginator(jobs, 2)
    page = request.POST.get('page')
    job_pages = p.get_page(page)

    context = {'jobs':job_pages,        
               'job_pages':job_pages,
               }
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return render(request, "partials/job_list.html", context)

    # Initial full page render
    return render(request, "search.html", context) 

@staff_member_required
def add_job_view(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JobForm()
    return render(request, "add-job.html", {'form':form})

def aboutview(request):

    return render(request, 'about.html')

def emp_job_view(request):

    return render(request, 'emp-job-form.html')
