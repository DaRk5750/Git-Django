from django.shortcuts import render, redirect
from app1.models import registation
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')


@csrf_exempt
def newregister(request):
    print("heep")
    if request.method == 'POST':
        u_name = request.POST['username']
        u_password = request.POST['password']
        u_age = request.POST['age']
        print(u_name, u_password, u_age)

        data = registation(username= u_name, password= u_password, age=u_age)
        data.save()
        return redirect('login')
        

        return render(request, 'index.html')

    return render(request, 'index.html')


@csrf_exempt
def loginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        data = registation.objects.get(username=username)
        if data.password == password:
            return render(request, 'index.html',{'username':data.username})

    return render(request, 'login.html')
