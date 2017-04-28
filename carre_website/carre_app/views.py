from django.shortcuts import render
from django.template import loader
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
from reportlab.pdfgen import canvas
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os

# Create your views here.
def index_home(request):
	context = {
        'name': 'index_home'
    }
	return render(request, 'carre_app/index_home.html', context)

def index_marque(request):
	context = {
        'name': 'index_marque'
    }
	return render(request, 'carre_app/index_marque.html', context)

def index_catalogue(request):
	context = {
        'name': 'index_catalogue'
    }
	return render(request, 'carre_app/index_catalogue.html', context)

def index_adressendtel(request):
	context = {
		'name': 'index_adressendtel'
	}
	return render(request, 'carre_app/index_adressendtel.html', context)

def index_location(request):
	context = {
		'name': 'index_location'
	}
	return render(request, 'carre_app/index_location.html', context)

def index_contacteznous(request):
	context = {
		'name': 'index_contacteznous'
	}
	return render(request, 'carre_app/index_contacteznous.html', context)

def index_sanitaire(request):
	articles = [
		{'url': 'a_1-1', 'name': 'name_a_1-1', 'ref': 'ref_a_1-1'},
		{'url': 'a_1-2', 'name': 'name_a_1-2', 'ref': 'ref_a_1-2'},
		{'url': 'a_1-3', 'name': 'name_a_1-3', 'ref': 'ref_a_1-3'},
		{'url': 'a_1-4', 'name': 'name_a_1-4', 'ref': 'ref_a_1-4'},
		{'url': 'a_1-5', 'name': 'name_a_1-5', 'ref': 'ref_a_1-5'},
		{'url': 'a_1-6', 'name': 'name_a_1-6', 'ref': 'ref_a_1-6'},
		{'url': 'a_1-7', 'name': 'name_a_1-7', 'ref': 'ref_a_1-7'},
		{'url': 'a_1-8', 'name': 'name_a_1-8', 'ref': 'ref_a_1-8'},
		{'url': 'a_1-9', 'name': 'name_a_1-9', 'ref': 'ref_a_1-9'},
		{'url': 'a_1-10', 'name': 'name_a_1-10', 'ref': 'ref_a_1-10'},
		{'url': 'a_1-11', 'name': 'name_a_1-11', 'ref': 'ref_a_1-11'},
		{'url': 'a_1-12', 'name': 'name_a_1-12', 'ref': 'ref_a_1-12'},
		{'url': 'a_1-13', 'name': 'name_a_1-13', 'ref': 'ref_a_1-13'},
		{'url': 'a_1-14', 'name': 'name_a_1-14', 'ref': 'ref_a_1-14'},
		{'url': 'a_1-15', 'name': 'name_a_1-15', 'ref': 'ref_a_1-15'},
		{'url': 'a_1-16', 'name': 'name_a_1-16', 'ref': 'ref_a_1-16'},
		{'url': 'a_1-17', 'name': 'name_a_1-17', 'ref': 'ref_a_1-17'},
		{'url': 'a_1-18', 'name': 'name_a_1-18', 'ref': 'ref_a_1-18'},
		{'url': 'a_1-19', 'name': 'name_a_1-19', 'ref': 'ref_a_1-19'},
		{'url': 'a_1-20', 'name': 'name_a_1-20', 'ref': 'ref_a_1-20'},
		{'url': 'a_1-21', 'name': 'name_a_1-21', 'ref': 'ref_a_1-21'},
		{'url': 'a_1-22', 'name': 'name_a_1-22', 'ref': 'ref_a_1-22'},
		{'url': 'a_1-23', 'name': 'name_a_1-23', 'ref': 'ref_a_1-23'},
		{'url': 'a_1-24', 'name': 'name_a_1-24', 'ref': 'ref_a_1-24'},
		{'url': 'a_1-25', 'name': 'name_a_1-25', 'ref': 'ref_a_1-25'},
		{'url': 'a_1-26', 'name': 'name_a_1-26', 'ref': 'ref_a_1-26'},
		{'url': 'a_1-27', 'name': 'name_a_1-27', 'ref': 'ref_a_1-27'},
		{'url': 'a_1-28', 'name': 'name_a_1-28', 'ref': 'ref_a_1-28'},
		{'url': 'a_1-29', 'name': 'name_a_1-29', 'ref': 'ref_a_1-29'},
		{'url': 'a_1-30', 'name': 'name_a_1-30', 'ref': 'ref_a_1-30'},
		{'url': 'a_1-31', 'name': 'name_a_1-31', 'ref': 'ref_a_1-31'},
		{'url': 'a_1-32', 'name': 'name_a_1-32', 'ref': 'ref_a_1-32'},
		{'url': 'a_1-33', 'name': 'name_a_1-33', 'ref': 'ref_a_1-33'},
		{'url': 'a_1-34', 'name': 'name_a_1-34', 'ref': 'ref_a_1-34'},
		{'url': 'a_1-35', 'name': 'name_a_1-35', 'ref': 'ref_a_1-35'},
	]
	paginator = Paginator(articles, 16)
	page = request.GET.get('page')
	try:
		articles_list = paginator.page(page)
	except PageNotAnInteger:
		articles_list = paginator.page(1)
	except EmptyPage:
		articles_list = paginator.page(paginator.num_pages)
	context = {
		'name': 'index_sanitaire',
		'articles_list': articles_list,
	}
	return render(request, 'carre_app/index_sanitaire.html', context)

def index_baignoiresetreceveurs(request):
	context = {
		'name': 'index_baignoiresetreceveurs'
	}
	return render(request, 'carre_app/index_baignoiresetreceveurs.html', context)

def index_miroirs(request):
	context = {
		'name': 'index_miroirs'
	}
	return render(request, 'carre_app/index_miroirs.html', context)

def index_meubles(request):
	context = {
		'name': 'index_meubles'
	}
	return render(request, 'carre_app/index_meubles.html', context)

def index_eviers(request):
	context = {
		'name': 'index_eviers'
	}
	return render(request, 'carre_app/index_eviers.html', context)

def index_robinetterie(request):
	context = {
		'name': 'index_robinetterie'
	}
	return render(request, 'carre_app/index_robinetterie.html', context)

def index_accessoires(request):
	context = {
		'name': 'index_accessoires'
	}
	return render(request, 'carre_app/index_accessoires.html', context)

def Catalogue(request):
	fs = FileSystemStorage()
	filename = 'carre_app/templates/carre_app/catalogue.pdf'
	if fs.exists(filename):
		with fs.open(filename) as pdf:
			response = HttpResponse(pdf, content_type='application/pdf')
			response['Content-Disposition'] = 'attachment; filename="catalogue.pdf"'
			return response
	else:
		return HttpResponseNotFound('The requested pdf was not found in our server.')