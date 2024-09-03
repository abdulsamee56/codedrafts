from django.shortcuts import render,  get_object_or_404, redirect
from .models import Projects
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import login

def home(request):
    return render(request, 'main/home.html')

def bank_management(request):
    # Retrieve all projects
    project = get_object_or_404(Projects, project_key='bank')

    # Pass the projects to the template
    return render(request, 'main/bank.html', {'project': project})


def cv_generator(request):
    project = get_object_or_404(Projects, project_key='cv')

    return render(request,'main/cv.html',{
        'project': project,
    })

def macro_tracker(request):
    project = get_object_or_404(Projects, project_key='macro')

    return render(request, 'main/calorie.html', {
        'project':project
    })

def about(request):
    return render(request,'main/aboutus.html')

def projects_view(request):
    beginner_projects = Projects.objects.filter(difficulty_level='Beginner')
    intermediate_projects = Projects.objects.filter(difficulty_level='Intermediate')
    advanced_projects = Projects.objects.filter(difficulty_level='Advanced')
    
    context = {
        'beginner_projects': beginner_projects,
        'intermediate_projects': intermediate_projects,
        'advanced_projects': advanced_projects,
    }
    
    return render(request, 'main/projects.html', context)

#Login Stuff 


def register_view(request):
    if request.method == "POST": 
        form = UserCreationForm(request.POST) 
        if form.is_valid(): 
            login(request, form.save())
            return redirect("/login") #update to accomoade posts:list, use /login for now
    else:
        form = UserCreationForm()
    return render(request, "main/register.html", { "form": form })

def login_view(request): 
    if request.method == "POST": 
        form = AuthenticationForm(data=request.POST)
        if form.is_valid(): 
            login(request, form.get_user())
            return redirect("/aboutus")  #update to accomoade posts:list, use /aboutus for now
    else: 
        form = AuthenticationForm()
    return render(request, "main/login.html", { "form": form })