from django.shortcuts import render
from django.template import loader

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
	return render(request, 'carre_app/index_adressendtel', context)

def index_location(request):
	context = {
		'name': 'index_location'
	}
	return render(request, 'carre_app/index_location', context)

def index_contacteznous(request):
	context = {
		'name': 'index_contacteznous'
	}
	return render(request, 'carre_app/index_contacteznous', context)

def index_sanitaire(request):
	context = {
		'name': 'index_sanitaire'
	}
	return render(request, 'carre_app/index_sanitaire', context)

def index_baignoiresetreceveurs(request):
	context = {
		'name': 'index_baignoiresetreceveurs'
	}
	return render(request, 'carre_app/index_baignoiresetreceveurs', context)

def index_miroirs(request):
	context = {
		'name': 'index_'
	}
	return render(request, 'carre_app/index_', context)