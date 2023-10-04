from django.shortcuts import render, redirect
import plotly.express as px
from django.db.models import Avg
from .models import Book, SearchHistory, MyBook
from django.contrib.auth import login, logout, authenticate
from .forms import RatingForm, BookCategory, CustomDataInput, RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here
@login_required(login_url="/login")
def home(request):
	search_history = SearchHistory.objects.filter(user=request.user)
	top = Book.objects.filter(pageCount__gte=650)

	context = {"top": top, "search_history": search_history[::-1][:5]}
	return render(request, 'core/home.html', context=context)


@login_required(login_url="/login")
def chart(request):
	book = Book.objects.all()
	rating = request.GET.get('Rating')

	if rating:
		book = Book.objects.filter(pageCount__gte=rating)

	fig = px.line(
		x=[b.title for b in book],
		y=[b.pageCount for b in book],
		title="Books Rating Line graph",
		labels={'x': 'Book Title', 'y': 'Ratings'}
	)

	chart = fig.to_html()

	context = {'chart': chart, 'form': RatingForm()}
	return render(request, 'core/chart.html', context=context)


@login_required(login_url="/login")
def avg_book(request):
	data = Book.objects.all()
	categories = request.GET.get('Category')

	if categories:
		data = Book.objects.filter(categories__icontains=categories)

	fig = px.bar(
		x=[b.title for b in data],
		y=[b.categories for b in data],
		title="Average book read",
		labels={'x': 'Book Title', 'y': 'categories'},
	)

	chart = fig.to_html()
	context = {'chart': chart, 'form': BookCategory()}
	return render(request, 'core/chart.html', context=context)


@login_required(login_url="/login")
def custom_data_generation(request):
	form = CustomDataInput()
	data = []
	category = request.GET.get('Book_Title')

	if category:
		data = Book.objects.filter(title__icontains=category).order_by('pageCount').reverse()
		search_obj = SearchHistory(user=request.user, history=category)
		search_obj.save()

	context = {'form': form, "data": data}
	return render(request, 'core/custom-data.html', context=context)


def sign_up(request):
	# if we get post req we'll make new user Form
	form = RegisterForm()
	if request.method == 'POST':
		form = RegisterForm(request.POST)

		if form.is_valid():
			user = form.save()
			if user is not None:
				login(request, user)
				messages.success(request, "User registered successfully")
				return redirect('/home')
			else:
				messages.success(request, "Can't registered user")
				return redirect('register')
		# else we will render the empty form on the screen

	context = {"form": form}
	return render(request, 'registration/sign_up.html', context=context)


@login_required(login_url="/login")
def history_data(request, pk):
	data = Book.objects.filter(categories__icontains=pk).order_by('pageCount').reverse()

	context = {'data': data}
	return render(request, "core/history.html", context=context)


