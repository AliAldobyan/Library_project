from django.shortcuts import render, redirect
from .models import Book
from .forms import SigninForm, MembershipForm, BookForm
from django.contrib.auth import login, authenticate, logout
from django.http import Http404
from django.db.models import Q
# Create your views here.

def create_membership(request):
    form = MembershipForm()
    if request.method == 'POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            return redirect("library-list")
    context = {
        "form":form,
    }
    return render(request, 'create_membership.html', context)

def signin(request):
    form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('library-list')
    context = {
        "form":form
    }
    return render(request, 'signin.html', context)

def signout(request):
    logout(request)
    return redirect("signin")

def library_list(request):
    if not (request.user.is_authenticated):
        return redirect('signin')

    books = Book.objects.all()

    query = request.GET.get("q")
    if query:
        books = books.filter(
            Q(name__icontains=query)|
            Q(genre__icontains=query)|
            Q(isbn__icontains=query)
            ).distinct()

    context = {
        "books": books,
    }
    return render(request, 'library_list.html', context)

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {
        "book": book,
    }
    return render(request, 'book_detail.html', context)


def create_book(request):
    if request.user.is_anonymous:
        return redirect('signin')
    if not request.user.is_staff:
        raise Http404
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('library-list')
    context = {
        "form":form,
    }
    return render(request, 'create_book.html', context)


def update_book(request, book_id):
    if request.user.is_anonymous:
        return redirect('signin')
    if not request.user.is_staff:
        return redirect('library-list')
    book = Book.objects.get(id=book_id)
    form = BookForm(instance=book)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('library-list')
    context = {
        "book": book,
        "form":form,
    }
    return render(request, 'update_book.html', context)

def delete_book(request, book_id):
    if request.user.is_anonymous:
        return redirect('signin')
    if not request.user.is_staff:
        return redirect('library-list')
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('library-list')
