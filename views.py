from .models import LoginForm
from django.shortcuts import redirect, render
from .models import Book,Contact
from .form import BookForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate

def home(request):
    return render(request,'home.html')


def adduser(request):
    if request.method=='POST':
        b=UserCreationForm(request.POST)
        b.save()
        return redirect('/')
    else:
        b=UserCreationForm()
        context={'form':b}
        return render(request,"adduser.html",context) 

def addbook(request):
    if request.method=='POST':
        book_name=request.POST.get("book_name")
        author_name=request.POST.get("author_name")
        pub_date=request.POST.get("pub_date")
        return_date=request.POST.get("return_date")
        cost=request.POST.get("cost")
        b=BookForm(request.POST)
        b.book_name=book_name
        b.author_name=author_name
        b.pub_date=pub_date
        b.return_date=return_date
        b.cost=cost
        b.save()
        return redirect("/blist")
    else:
        return render(request,"addbook.html")

def booklist(request):
    blist=Book.objects.all()
    d={"bl":blist}
    return render(request,"booklist.html",d)


def delete_book(request):
    bid=request.GET.get("id")
    book=Book.objects.get(id=bid)
    book.delete()
    return redirect("/blist")


def edit_book(request,id):
    book=Book.objects.get(id=id)
    if request.method=='POST':
        b=BookForm(request.POST,instance=book)
        b.save()
        return redirect("/blist")
    else:
        b=BookForm(instance=book)
        context={'form':b}
        return render(request,"updatebook.html",context)


def login_view(request):
    if request.method=='POST':  
        uname=request.POST.get("username")
        passw=request.POST.get("password") 
        user=authenticate(request,username=uname,password=passw)
        if user is not None:
            request.session["uid"]=user.id
            login(request,user)
            return redirect("/")
        else: 
            b=LoginForm
            context={'form':b}
            return render(request,"login.html",context)
    else:
        b=LoginForm
        context={'form':b}
        return render(request,"login.html",context)


def logout_view(request):
    logout(request)
    return redirect("/") 


def contact(request):
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        content=request.POST.get("content")
        print(name,email,phone,content)
        contact=Contact(name=name,email=email,phone=phone,content=content)
        contact.save()
    return render(request,"contact.html")