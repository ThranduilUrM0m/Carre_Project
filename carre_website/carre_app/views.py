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

def index_collectionsalledebains(request):
	context = {
		'name': 'index_collectionsalledebains'
	}
	return render(request, 'carre_app/index_collectionsalledebains.html', context)

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
	articles = [
		{'url': 'a_2-1', 'name': 'name_a_2-1', 'ref': 'ref_a_2-1'},
		{'url': 'a_2-2', 'name': 'name_a_2-2', 'ref': 'ref_a_2-2'},
		{'url': 'a_2-3', 'name': 'name_a_2-3', 'ref': 'ref_a_2-3'},
		{'url': 'a_2-4', 'name': 'name_a_2-4', 'ref': 'ref_a_2-4'},
		{'url': 'a_2-5', 'name': 'name_a_2-5', 'ref': 'ref_a_2-5'},
		{'url': 'a_2-6', 'name': 'name_a_2-6', 'ref': 'ref_a_2-6'},
		{'url': 'a_2-7', 'name': 'name_a_2-7', 'ref': 'ref_a_2-7'},
		{'url': 'a_2-8', 'name': 'name_a_2-8', 'ref': 'ref_a_2-8'},
		{'url': 'a_2-9', 'name': 'name_a_2-9', 'ref': 'ref_a_2-9'},
		{'url': 'a_2-10', 'name': 'name_a_2-10', 'ref': 'ref_a_2-10'},
		{'url': 'a_2-11', 'name': 'name_a_2-11', 'ref': 'ref_a_2-11'},
		{'url': 'a_2-12', 'name': 'name_a_2-12', 'ref': 'ref_a_2-12'},
		{'url': 'a_2-13', 'name': 'name_a_2-13', 'ref': 'ref_a_2-13'},
		{'url': 'a_2-14', 'name': 'name_a_2-14', 'ref': 'ref_a_2-14'},
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
		'name': 'index_baignoiresetreceveurs',
		'articles_list': articles_list,
	}
	return render(request, 'carre_app/index_baignoiresetreceveurs.html', context)

def index_miroirs(request):
	articles = [
		{'url': 'a_3-1', 'name': 'name_a_3-1', 'ref': 'ref_a_3-1'},
		{'url': 'a_3-2', 'name': 'name_a_3-2', 'ref': 'ref_a_3-2'},
		{'url': 'a_3-3', 'name': 'name_a_3-3', 'ref': 'ref_a_3-3'},
		{'url': 'a_3-4', 'name': 'name_a_3-4', 'ref': 'ref_a_3-4'},
		{'url': 'a_3-5', 'name': 'name_a_3-5', 'ref': 'ref_a_3-5'},
		{'url': 'a_3-6', 'name': 'name_a_3-6', 'ref': 'ref_a_3-6'},
		{'url': 'a_3-7', 'name': 'name_a_3-7', 'ref': 'ref_a_3-7'},
		{'url': 'a_3-8', 'name': 'name_a_3-8', 'ref': 'ref_a_3-8'},
		{'url': 'a_3-9', 'name': 'name_a_3-9', 'ref': 'ref_a_3-9'},
		{'url': 'a_3-10', 'name': 'name_a_3-10', 'ref': 'ref_a_3-10'},
		{'url': 'a_3-11', 'name': 'name_a_3-11', 'ref': 'ref_a_3-11'},
		{'url': 'a_3-12', 'name': 'name_a_3-12', 'ref': 'ref_a_3-12'},
		{'url': 'a_3-13', 'name': 'name_a_3-13', 'ref': 'ref_a_3-13'},
		{'url': 'a_3-14', 'name': 'name_a_3-14', 'ref': 'ref_a_3-14'},
		{'url': 'a_3-15', 'name': 'name_a_3-15', 'ref': 'ref_a_3-15'},
		{'url': 'a_3-16', 'name': 'name_a_3-16', 'ref': 'ref_a_3-16'},
		{'url': 'a_3-17', 'name': 'name_a_3-17', 'ref': 'ref_a_3-17'},
		{'url': 'a_3-18', 'name': 'name_a_3-18', 'ref': 'ref_a_3-18'},
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
		'name': 'index_miroirs',
		'articles_list': articles_list,
	}
	return render(request, 'carre_app/index_miroirs.html', context)

def index_meubles(request):
	articles = [
		{'url': 'a_4-1', 'name': 'name_a_4-1', 'ref': 'ref_a_4-1'},
		{'url': 'a_4-2', 'name': 'name_a_4-2', 'ref': 'ref_a_4-2'},
		{'url': 'a_4-3', 'name': 'name_a_4-3', 'ref': 'ref_a_4-3'},
		{'url': 'a_4-4', 'name': 'name_a_4-4', 'ref': 'ref_a_4-4'},
		{'url': 'a_4-5', 'name': 'name_a_4-5', 'ref': 'ref_a_4-5'},
		{'url': 'a_4-6', 'name': 'name_a_4-6', 'ref': 'ref_a_4-6'},
		{'url': 'a_4-7', 'name': 'name_a_4-7', 'ref': 'ref_a_4-7'},
		{'url': 'a_4-8', 'name': 'name_a_4-8', 'ref': 'ref_a_4-8'},
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
		'name': 'index_meubles',
		'articles_list': articles_list,
	}
	return render(request, 'carre_app/index_meubles.html', context)

def index_eviers(request):
	articles = [
		{'url': 'a_5-1', 'name': 'name_a_5-1', 'ref': 'ref_a_5-1'},
		{'url': 'a_5-2', 'name': 'name_a_5-2', 'ref': 'ref_a_5-2'},
		{'url': 'a_5-3', 'name': 'name_a_5-3', 'ref': 'ref_a_5-3'},
		{'url': 'a_5-4', 'name': 'name_a_5-4', 'ref': 'ref_a_5-4'},
		{'url': 'a_5-5', 'name': 'name_a_5-5', 'ref': 'ref_a_5-5'},
		{'url': 'a_5-6', 'name': 'name_a_5-6', 'ref': 'ref_a_5-6'},
		{'url': 'a_5-7', 'name': 'name_a_5-7', 'ref': 'ref_a_5-7'},
		{'url': 'a_5-8', 'name': 'name_a_5-8', 'ref': 'ref_a_5-8'},
		{'url': 'a_5-9', 'name': 'name_a_5-9', 'ref': 'ref_a_5-9'},
		{'url': 'a_5-10', 'name': 'name_a_5-10', 'ref': 'ref_a_5-10'},
		{'url': 'a_5-11', 'name': 'name_a_5-11', 'ref': 'ref_a_5-11'},
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
		'name': 'index_eviers',
		'articles_list': articles_list,
	}
	return render(request, 'carre_app/index_eviers.html', context)

def index_robinetterie(request):
	articles = [
		{'url': 'a_6-1', 'name': 'name_a_6-1', 'ref': 'ref_a_6-1'},
		{'url': 'a_6-2', 'name': 'name_a_6-2', 'ref': 'ref_a_6-2'},
		{'url': 'a_6-3', 'name': 'name_a_6-3', 'ref': 'ref_a_6-3'},
		{'url': 'a_6-4', 'name': 'name_a_6-4', 'ref': 'ref_a_6-4'},
		{'url': 'a_6-5', 'name': 'name_a_6-5', 'ref': 'ref_a_6-5'},
		{'url': 'a_6-6', 'name': 'name_a_6-6', 'ref': 'ref_a_6-6'},
		{'url': 'a_6-7', 'name': 'name_a_6-7', 'ref': 'ref_a_6-7'},
		{'url': 'a_6-8', 'name': 'name_a_6-8', 'ref': 'ref_a_6-8'},
		{'url': 'a_6-9', 'name': 'name_a_6-9', 'ref': 'ref_a_6-9'},
		{'url': 'a_6-10', 'name': 'name_a_6-10', 'ref': 'ref_a_6-10'},
		{'url': 'a_6-11', 'name': 'name_a_6-11', 'ref': 'ref_a_6-11'},
		{'url': 'a_6-12', 'name': 'name_a_6-12', 'ref': 'ref_a_6-12'},
		{'url': 'a_6-13', 'name': 'name_a_6-13', 'ref': 'ref_a_6-13'},
		{'url': 'a_6-14', 'name': 'name_a_6-14', 'ref': 'ref_a_6-14'},
		{'url': 'a_6-15', 'name': 'name_a_6-15', 'ref': 'ref_a_6-15'},
		{'url': 'a_6-16', 'name': 'name_a_6-16', 'ref': 'ref_a_6-16'},
		{'url': 'a_6-17', 'name': 'name_a_6-17', 'ref': 'ref_a_6-17'},
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
		'name': 'index_robinetterie',
		'articles_list': articles_list,
	}
	return render(request, 'carre_app/index_robinetterie.html', context)

def index_accessoires(request):
	articles = [
		{'url': 'a_7-1', 'name': 'name_a_7-1', 'ref': 'ref_a_7-1'},
		{'url': 'a_7-2', 'name': 'name_a_7-2', 'ref': 'ref_a_7-2'},
		{'url': 'a_7-3', 'name': 'name_a_7-3', 'ref': 'ref_a_7-3'},
		{'url': 'a_7-4', 'name': 'name_a_7-4', 'ref': 'ref_a_7-4'},
		{'url': 'a_7-5', 'name': 'name_a_7-5', 'ref': 'ref_a_7-5'},
		{'url': 'a_7-6', 'name': 'name_a_7-6', 'ref': 'ref_a_7-6'},
		{'url': 'a_7-7', 'name': 'name_a_7-7', 'ref': 'ref_a_7-7'},
		{'url': 'a_7-8', 'name': 'name_a_7-8', 'ref': 'ref_a_7-8'},
		{'url': 'a_7-9', 'name': 'name_a_7-9', 'ref': 'ref_a_7-9'},
		{'url': 'a_7-10', 'name': 'name_a_7-10', 'ref': 'ref_a_7-10'},
		{'url': 'a_7-11', 'name': 'name_a_7-11', 'ref': 'ref_a_7-11'},
		{'url': 'a_7-12', 'name': 'name_a_7-12', 'ref': 'ref_a_7-12'},
		{'url': 'a_7-13', 'name': 'name_a_7-13', 'ref': 'ref_a_7-13'},
		{'url': 'a_7-14', 'name': 'name_a_7-14', 'ref': 'ref_a_7-14'},
		{'url': 'a_7-15', 'name': 'name_a_7-15', 'ref': 'ref_a_7-15'},
		{'url': 'a_7-16', 'name': 'name_a_7-16', 'ref': 'ref_a_7-16'},
		{'url': 'a_7-17', 'name': 'name_a_7-17', 'ref': 'ref_a_7-17'},
		{'url': 'a_7-18', 'name': 'name_a_7-18', 'ref': 'ref_a_7-18'},
		{'url': 'a_7-19', 'name': 'name_a_7-19', 'ref': 'ref_a_7-19'},
		{'url': 'a_7-20', 'name': 'name_a_7-20', 'ref': 'ref_a_7-20'},
		{'url': 'a_7-21', 'name': 'name_a_7-21', 'ref': 'ref_a_7-21'},
		{'url': 'a_7-22', 'name': 'name_a_7-22', 'ref': 'ref_a_7-22'},
		{'url': 'a_7-23', 'name': 'name_a_7-23', 'ref': 'ref_a_7-23'},
		{'url': 'a_7-24', 'name': 'name_a_7-24', 'ref': 'ref_a_7-24'},
		{'url': 'a_7-25', 'name': 'name_a_7-25', 'ref': 'ref_a_7-25'},
		{'url': 'a_7-26', 'name': 'name_a_7-26', 'ref': 'ref_a_7-26'},
		{'url': 'a_7-27', 'name': 'name_a_7-27', 'ref': 'ref_a_7-27'},
		{'url': 'a_7-28', 'name': 'name_a_7-28', 'ref': 'ref_a_7-28'},
		{'url': 'a_7-29', 'name': 'name_a_7-29', 'ref': 'ref_a_7-29'},
		{'url': 'a_7-30', 'name': 'name_a_7-30', 'ref': 'ref_a_7-30'},
		{'url': 'a_7-31', 'name': 'name_a_7-31', 'ref': 'ref_a_7-31'},
		{'url': 'a_7-32', 'name': 'name_a_7-32', 'ref': 'ref_a_7-32'},
		{'url': 'a_7-33', 'name': 'name_a_7-33', 'ref': 'ref_a_7-33'},
		{'url': 'a_7-34', 'name': 'name_a_7-34', 'ref': 'ref_a_7-34'},
		{'url': 'a_7-35', 'name': 'name_a_7-35', 'ref': 'ref_a_7-35'},
		{'url': 'a_7-36', 'name': 'name_a_7-36', 'ref': 'ref_a_7-36'},
		{'url': 'a_7-37', 'name': 'name_a_7-37', 'ref': 'ref_a_7-37'},
		{'url': 'a_7-38', 'name': 'name_a_7-38', 'ref': 'ref_a_7-38'},
		{'url': 'a_7-39', 'name': 'name_a_7-39', 'ref': 'ref_a_7-39'},
		{'url': 'a_7-40', 'name': 'name_a_7-40', 'ref': 'ref_a_7-40'},
		{'url': 'a_7-41', 'name': 'name_a_7-41', 'ref': 'ref_a_7-41'},
		{'url': 'a_7-42', 'name': 'name_a_7-42', 'ref': 'ref_a_7-42'},
		{'url': 'a_7-43', 'name': 'name_a_7-43', 'ref': 'ref_a_7-43'},
		{'url': 'a_7-44', 'name': 'name_a_7-44', 'ref': 'ref_a_7-44'},
		{'url': 'a_7-45', 'name': 'name_a_7-45', 'ref': 'ref_a_7-45'},
		{'url': 'a_7-46', 'name': 'name_a_7-46', 'ref': 'ref_a_7-46'},
		{'url': 'a_7-47', 'name': 'name_a_7-47', 'ref': 'ref_a_7-47'},
		{'url': 'a_7-48', 'name': 'name_a_7-48', 'ref': 'ref_a_7-48'},
		{'url': 'a_7-49', 'name': 'name_a_7-49', 'ref': 'ref_a_7-49'},
		{'url': 'a_7-50', 'name': 'name_a_7-50', 'ref': 'ref_a_7-50'},
		{'url': 'a_7-51', 'name': 'name_a_7-51', 'ref': 'ref_a_7-51'},
		{'url': 'a_7-52', 'name': 'name_a_7-52', 'ref': 'ref_a_7-52'},
		{'url': 'a_7-53', 'name': 'name_a_7-53', 'ref': 'ref_a_7-53'},
		{'url': 'a_7-54', 'name': 'name_a_7-54', 'ref': 'ref_a_7-54'},
		{'url': 'a_7-55', 'name': 'name_a_7-55', 'ref': 'ref_a_7-55'},
		{'url': 'a_7-56', 'name': 'name_a_7-56', 'ref': 'ref_a_7-56'},
		{'url': 'a_7-57', 'name': 'name_a_7-57', 'ref': 'ref_a_7-57'},
		{'url': 'a_7-58', 'name': 'name_a_7-58', 'ref': 'ref_a_7-58'},
		{'url': 'a_7-59', 'name': 'name_a_7-59', 'ref': 'ref_a_7-59'},
		{'url': 'a_7-60', 'name': 'name_a_7-60', 'ref': 'ref_a_7-60'},
		{'url': 'a_7-61', 'name': 'name_a_7-61', 'ref': 'ref_a_7-61'},
		{'url': 'a_7-62', 'name': 'name_a_7-62', 'ref': 'ref_a_7-62'},
		{'url': 'a_7-63', 'name': 'name_a_7-63', 'ref': 'ref_a_7-63'},
		{'url': 'a_7-64', 'name': 'name_a_7-64', 'ref': 'ref_a_7-64'},
		{'url': 'a_7-65', 'name': 'name_a_7-65', 'ref': 'ref_a_7-65'},
		{'url': 'a_7-66', 'name': 'name_a_7-66', 'ref': 'ref_a_7-66'},
		{'url': 'a_7-67', 'name': 'name_a_7-67', 'ref': 'ref_a_7-67'},
		{'url': 'a_7-68', 'name': 'name_a_7-68', 'ref': 'ref_a_7-68'},
		{'url': 'a_7-69', 'name': 'name_a_7-69', 'ref': 'ref_a_7-69'},
		{'url': 'a_7-70', 'name': 'name_a_7-70', 'ref': 'ref_a_7-70'},
		{'url': 'a_7-71', 'name': 'name_a_7-71', 'ref': 'ref_a_7-71'},
		{'url': 'a_7-72', 'name': 'name_a_7-72', 'ref': 'ref_a_7-72'},
		{'url': 'a_7-73', 'name': 'name_a_7-73', 'ref': 'ref_a_7-73'},
		{'url': 'a_7-74', 'name': 'name_a_7-74', 'ref': 'ref_a_7-74'},
		{'url': 'a_7-75', 'name': 'name_a_7-75', 'ref': 'ref_a_7-75'},
		{'url': 'a_7-76', 'name': 'name_a_7-76', 'ref': 'ref_a_7-76'},
		{'url': 'a_7-77', 'name': 'name_a_7-77', 'ref': 'ref_a_7-77'},
		{'url': 'a_7-78', 'name': 'name_a_7-78', 'ref': 'ref_a_7-78'},
		{'url': 'a_7-79', 'name': 'name_a_7-79', 'ref': 'ref_a_7-79'},
		{'url': 'a_7-80', 'name': 'name_a_7-80', 'ref': 'ref_a_7-80'},
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
		'name': 'index_accessoires',
		'articles_list': articles_list,
	}
	return render(request, 'carre_app/index_accessoires.html', context)

def Catalogue(request):
	fs = FileSystemStorage()
	filename = 'carre_app/templates/carre_app/catalogue.pdf'
	if fs.exists(filename):
		with fs.open(filename, 'rb') as pdf:
			response = HttpResponse(pdf.read(), content_type='application/pdf')
			response['Content-Disposition'] = 'filename="catalogue.pdf"'
			return response
	else:
		return HttpResponseNotFound('The requested pdf was not found in our server.')