from django import forms
from rango.models import *

class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=Category._meta.get_field('name').max_length, help_text="Please enter the category name.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	# An inline class to provide additional information on the form.
	class Meta:
		# Provide an association between the ModelForm and a model
		model = Category
		fields = ('name',)

class PageForm(forms.ModelForm):
	title = forms.CharField(max_length=128, help_text="Please enter the page name.")
	url = forms.CharField(max_length=200, help_text="Please enter the page url.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

	class Meta:
		# Provide an assocation between the ModelForm and a model
		model = Page
		exclude = ('category',)

	def clean(self):
		cleaned_data = self.cleaned_data
		url = cleaned_data.get('url')

		# If url is not empty and doesn't start with 'http://',
		# then prepend 'http://'.
		if url and not url.startswith('http://'):
			url = 'http://' + url
			cleaned_data['url'] = url

			return cleaned_data