from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Task
from .forms import TaskForm

from django.utils.timezone import now


# Create your views here.
# def index(request):
#     return render(request, 'index.html')


def index(request):
    # Retrieve all to-do items ordered by date (newest first)
    if request.user.is_authenticated:    
        item_list = Task.objects.filter(user=request.user).order_by("-create_time")
        context ={
            'item_list':item_list
        }
        return render(request, 'index.html', context)
    else:
        return redirect('login')

def add_task(request):
    if request.method=='POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')

        create_time = now()

        Task.objects.create(
            title=title,
            description=description,
            due_date=due_date,
            create_time=create_time, 
            user=request.user)
        
    return redirect('/')


def remove_task(request,pk):
    rem_task = get_object_or_404(Task, pk=pk)
    rem_task.delete()
    return redirect('/')


def edit_task(request,pk):
    pass


def search_task(request):
    q = request.GET.get('query', '')
    if q:
        item_list = Task.objects.filter(title__icontains=q)
    else:
        item_list = Task.objects.all().order_by("-create_time")

    context = {
        'item_list':item_list
    }
    return render(request,'index.html', context)


def user_register(request):
    context = {}
    if request.method=="POST":
        username = request.POST['uname']
        useremail = request.POST['uemail']
        pass1 = request.POST['upass1']
        pass2 = request.POST['upass2']

        if pass1 == pass2:
            if User.objects.filter(email=useremail).exists():
                messages.error(request, "This email is already registered. Please try another one!")
                return render(request,'Register.html')
            else:        
                try:
                    user = User.objects.create_user(username=username, email=useremail, password=pass1)
                    user.save()
                    login(request, user)
                    return redirect('/')
                except Exception as e:
                    messages.error(request, "An error occurred during registration: " + str(e))
                    return render(request,'Register.html')
        else:
            messages.error(request, "Passwords are not macthing!")
            return render(request,'Register.html')
    
    else:
        return render(request, 'Register.html')

def user_login(request):
    if request.method=='POST':
        identifier = request.POST['uemail']
        password = request.POST['upass']
       
        user = authenticate(request, username=identifier, password=password)

        if not user:
            try:               
                # Find username using email
                u = User.objects.get(email=identifier)

                user = authenticate(request, username=u.username, password=password)
            except User.DoesNotExist:
                user = None

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'Login.html')
    
    else:
        return render(request, 'Login.html')
    
def user_logout(request):
    logout(request)
    return redirect('login')