from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm  #from . import forms da yazılabilir
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None) #GET veya POST request kontrolüne gerek kalmadan işlem yapılır
    if form.is_valid():
    
        username = form.cleaned_data.get("username")  #clean metodundaki değerleri alabilmek için
        password = form.cleaned_data.get("password") #CLEAN METODUNU ÇAĞIRMAK İÇİN ÖZEL FONKSİYON.#FORM TRUE OLURSA İŞLEM YAPILIR
                        
        newUser = User(username = username)
        newUser.set_password(password)

        newUser.save()
        login(request,newUser)
        messages.info(request,"Başarı ile Kayıt Oldunuz")
        return redirect("transferapp:index")
    context = {
    "form" : form
    }
    return render(request,"register.html",context)        

   
    

def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
    "form" : form
    }

    if form.is_valid(): #otomatikman clean'daki datalara ulaşılır bu fonksiyonla
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username,password = password)
        if user is None : 
            messages.info(request,"Kullanıcı adı veya Parola Hatalı")
            return render(request,"login.html",context)

        messages.success(request,"Başarı ile Giriş Yaptınız")
        login(request,user)
        return redirect("transferapp:index")

    
    return render(request,"login.html",context)
def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("transferapp:index")





def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Şifreniz Başarıyla Değiştirilmiştir')
            return redirect('transferapp:index')
        else:
            messages.error(request, 'Lütfen Aşağıdaki Hatayı Düzeltin')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })