
from django.shortcuts import redirect, render,HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from datetime import date
from django.contrib.auth.decorators import login_required
from .forms import IssueBookForm
from .models import IssuedBook


# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
@login_required(login_url='/admin_login')
def a_home(request):
    return render(request,'a_home.html')
def s_home(request):
    return render(request,'s_home.html')
def add_book(request):
    if request.method == "POST":
        name = request.POST['name']
        author = request.POST['author']
        isbn = request.POST['isbn']
        category = request.POST['category']

        books = Book.objects.create(name=name, author=author, isbn=isbn, category=category)
        books.save()
        alert = True
        return render(request, "add_book.html", {'alert':alert})
    return render(request, "add_book.html")
def view_books(request):
    books = Book.objects.all()
    return render(request, "view_books.html", {'books':books})
def view_students(request):
    students = Students.objects.all()
    return render(request, "view_students.html", {'students':students})

def issue_book(request):
    if request.method == "POST":
        form = IssueBookForm(request.POST)
        if form.is_valid():
            issued_book = form.save(commit=False)
            issued_book.isbn = form.cleaned_data['isbn2'].isbn
            issued_book.student_id = form.cleaned_data['name2'].roll_no
            issued_book.save()
            return redirect('/view_issued_books')  # Redirect after successful form submission
        else:
            print(form.errors)  # Print form errors to the console for debugging
    else:
        form = IssueBookForm()
    return render(request, "issue_book.html", {'form': form})
def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect("/a_home")
            else:
                return HttpResponse("You are not an admin.")
        else:
            alert = True
            return render(request, "admin_login.html", {'alert':alert})
    return render(request, "admin_login.html")
def student_registration(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        branch = request.POST['branch']
        classroom = request.POST['classroom']
        roll_no = request.POST['roll_no']
        image = request.FILES['image']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            passnotmatch = True
            return render(request, "student_registration.html", {'passnotmatch':passnotmatch})

        user = User.objects.create_user(username=username, email=email, password=password,first_name=first_name, last_name=last_name)
        student = Students.objects.create(user=user, phone=phone, branch=branch, classroom=classroom,roll_no=roll_no, image=image)
        user.save()
        student.save()
        alert = True
        return render(request, "student_registration.html", {'alert':alert})
    return render(request, "student_registration.html")

def student_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return HttpResponse("You are not a student!!")
            else:
                return redirect("/s_home")
        else:
            alert = True
            return render(request, "student_login.html", {'alert':alert})
    return render(request, "student_login.html")

@login_required(login_url = '/student_login.html')
def profile(request):
    return render(request, "profile.html")
def view_issued_books(request):
    issued_books = IssuedBook.objects.all()
    return render(request, "view_issued_books.html", {'issued_books': issued_books})

@login_required(login_url = '/student_login')
def edit_profile(request):
    student = Students.objects.get(user=request.user)
    if request.method == "POST":
        email = request.POST['email']
        phone = request.POST['phone']
        branch = request.POST['branch']
        classroom = request.POST['classroom']
        roll_no = request.POST['roll_no']

        student.user.email = email
        student.phone = phone
        student.branch = branch
        student.classroom = classroom
        student.roll_no = roll_no
        student.user.save()
        student.save()
        alert = True
        return render(request, "edit_profile.html", {'alert':alert})
    return render(request, "edit_profile.html")

def change_password(request):
    if request.method == "POST":
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(current_password):
                u.set_password(new_password)
                u.save()
                alert = True
                return render(request, "change_password.html", {'alert':alert})
            else:
                currpasswrong = True
                return render(request, "change_password.html", {'currpasswrong':currpasswrong})
        except:
            pass
    return render(request, "change_password.html")

def delete_book(request, myid):
    books = Book.objects.filter(id=myid)
    books.delete()
    return redirect("/view_books")

def delete_student(request, myid):
    students = Students.objects.filter(id=myid)
    students.delete()
    return redirect("/view_students")

def Logout(request):
    logout(request)
    return redirect ("/")
