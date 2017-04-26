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
		'name': 'index_miroirs'
	}
	return render(request, 'carre_app/index_miroirs', context)

def index_meubles(request):
	context = {
		'name': 'index_meubles'
	}
	return render(request, 'carre_app/index_meubles', context)

def index_eviers(request):
	context = {
		'name': 'index_eviers'
	}
	return render(request, 'carre_app/index_eviers', context)

def index_robinetterie(request):
	context = {
		'name': 'index_robinetterie'
	}
	return render(request, 'carre_app/index_robinetterie', context)

def index_accessoires(request):
	context = {
		'name': 'index_accessoires'
	}
	return render(request, 'carre_app/index_accessoires', context)