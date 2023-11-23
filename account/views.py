from django.shortcuts import render
from account.forms.SignupForm import SignupForm
from account.forms.SigninForm import SigninForm
# from account.forms.UsersForm import UserForm
from django.http import HttpResponse
import bcrypt
from django.shortcuts import redirect
from django.contrib import messages
from account.models import Account


# Create your views here.

def signin(request):
    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            # salt = bcrypt.gensalt(rounds=15)
            # hashedPassword = bcrypt.hashpw( (form.cleaned_data['password']).encode(), salt)
            account = Account.objects.filter(
            username = form.cleaned_data['username'], 
            password = form.cleaned_data['password'],
            ).first()
            if account:
                request.session['username'] = form.cleaned_data['username']
                return redirect("/dashboard")
            else:
                form = SigninForm()
                messages.success(request,f"User Account not found. Please Check your credentials")
                return render(request,"signin.html",{'form': form}) 
    else:
         form = SigninForm()
         return render(request,"signin.html",{'form': form})

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            # account = form.save(commit=False)
            # # salt = bcrypt.gensalt(rounds=15)
            # # account.password = bcrypt.hashpw( (form.cleaned_data['password']).encode(), salt)
            form.save()
            messages.success(request,f"Your Account has been created Successfully.")
            return redirect("/signup")
        else:
            form = SignupForm()
            return render(request,"signup.html",{'form': form}) 
    else:
        form = SignupForm()
        return render(request,"signup.html",{'form': form})
        # return render(request,"signup.html")

def dashboard(request):
        
        if request.session['username']:
            try:
                return render(request,"statistics.html",{'year':request.session['year'],'term':request.session['term']})
            except:
                return render(request,"statistics.html")
        else:
         form = SigninForm()
         return render(request,"signin.html",{'form': form})
        
     


def recoverPassword(request):
    return render(request,"recoverpassword.html")

def userprofile(request):
    return render(request,"user.html")
    # if request.method == "POST":
    #     form = UserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request,f"Successfully Submitted.")
    #         return redirect("/userprofile")
    #     else:
    #        return render(request,"user.html",{'form': form}) 
    # else:
    #     form = UserForm()
    #     newlyCreatedUser = User.objects.all().latest('id')
    #     return render(request,"user.html",{'form': form,'user':newlyCreatedUser})


    