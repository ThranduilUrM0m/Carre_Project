from django.shortcuts import render
from django.template import loader
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
from reportlab.pdfgen import canvas
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
	context = {
		'name': 'index_sanitaire'
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