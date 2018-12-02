from django.contrib import admin
from rango.models import *

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')
	search_fields = ['title']

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)