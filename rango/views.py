from django.shortcuts import render
from django.http import HttpResponse
from rango.models import *

def index(request):
	# Query the database for a list of all categories currently stored
	# Order the categories by no. of likes in descending order
	# Retrieve the top 5 only or all if less than 5
	# Place the list in our context_dict dictionary
	# that will be passed on to the template engine

	category_list = Category.objects.order_by('-like')[:5]
	context_dict = {'categories': category_list}

	return render(request, 'rango/index.html', context=context_dict)

def about(request):
	return render(request, 'rango/about.html')

def show_category(request, category_name_slug):
	# Create a context dictionary which we can pass
	# to the templat rendering engine
	context_dict = {}

	try:
		# Can we find a category name slug with the given name?
		# If we can't, the .get() method raises a DoesNotExist exception
		# so the .get() method returns one model instance or raises an exception.
		category = Category.objects.get(slug=category_name_slug)

		# Retrieve all of the associated pages.
		# Note that filter() will return a list of pages objects or an empty list
		pages = Page.objects.filter(category=category)

		# Adds our results list to the template context under name pages.
		context_dict['pages'] = pages

		# We also add the category object from
		# the database to the context dictionary.
		# We'll use this in the template to verify that the category exists.
		context_dict['category'] = category
	except Category.DoesNotExist:
		context_dict['category'] = None
		context_dict['pages'] = None

	return render(request, 'rango/category.html', context_dict)