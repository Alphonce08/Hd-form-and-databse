from.model import Student
from django.shortcuts import render, redirect

def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        idnum = request.POST.get('idnum')





        submit_data = Student(name = name, email = email, idnum = idnum)
        submit_data.save()
        return redirect('/')
    return render(request, "register.html")


def homepage(request):
    return render(request, 'home.html')
def registerpage(request):
    return render(request, 'register.html')