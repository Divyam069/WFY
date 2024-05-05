from django.shortcuts import render, redirect
from .models import *
from .forms import UserRegisterForm

# Create your views here.

def productNavView():
    productdata = ProductModel.objects.all()
    return productdata
def sessionDataView(request):
    email_1=request.session['user']
    dictData={'email':email_1}
    return dictData
def CatergoryView(request):
    if 'user' in request.session:
        categoryData=CategroyModel.objects.all()
        sessionDataView1=sessionDataView(request)
        productNavData=productNavView()
        return render(request,'Index.html',{categoryData:categoryData,'sessionDataView1':sessionDataView1,'productNavData':productNavData})
    else:
        categoryData=CategroyModel.objects.all()
        productNavData=productNavView()
        return render(request,'Index.html',{'categoryData':categoryData,'productNavData':productNavData})
def register(request):
    obj=UserRegisterForm(request.POST)
    if obj.is_valid():
        data=Register.objects.all().filter(Email=request.POST['Email'])
        if len(data)<=0:
            obj.save()
            return redirect('Category')
        else:
            return render(request,'Register.html',{'error':'Email already exists'}) 
    return render(request,'Register.html')
def login(request):
    if request.POST:
        Email_1=request.POST['Email']
        Password_1=request.POST['password']
        try:
            data=Register.objects.get(Email=Email_1,password=Password_1)
            if data:
                request.session['user']=Email_1
                request.session['userId']=data.pk
                print(request.session['user'])
                return redirect('Category')
        except:
            return redirect('login')
    return render(request,'Login.html')
def logout(request):
    if 'user' in request.session:
        del request.session['user']
        return redirect('Category')
    return redirect('login')










