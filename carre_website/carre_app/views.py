from django.shortcuts import render
from django.template import loader
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
from reportlab.pdfgen import canvas
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, Collection, Comporter, Categorie, Subcategorie, TypeProduct
import os
from collections import Counter

# Create your views here.
def index_home(request):
	Categorie_list = Categorie.objects.all()
	Subcategorie_list = Subcategorie.objects.all()
	Collection_list = Collection.objects.all()
	Comporter_list = Comporter.objects.all()
	Categorie_withCollec_list = Categorie.objects.filter(id_categorie__in=Comporter_list)
	Collection_withCat_list = Collection.objects.filter(id_collection__in=Comporter_list)
	context = {
		'Categorie_list': Categorie_list,
		'Subcategorie_list': Subcategorie_list,
		'Collection_list': Collection_list,
		'Comporter_list': Comporter_list,
		'Categorie_withCollec_list': Categorie_withCollec_list,
		'Collection_withCat_list': Collection_withCat_list,
    }
	return render(request, 'carre_app/index_home.html', context)

def index_marque(request):
	Categorie_list = Categorie.objects.all()
	Subcategorie_list = Subcategorie.objects.all()
	Collection_list = Collection.objects.all()
	Comporter_list = Comporter.objects.all()
	Categorie_withCollec_list = Categorie.objects.filter(id_categorie__in=Comporter_list)
	Collection_withCat_list = Collection.objects.filter(id_collection__in=Comporter_list)
	context = {
		'Categorie_list': Categorie_list,
		'Subcategorie_list': Subcategorie_list,
		'Collection_list': Collection_list,
		'Comporter_list': Comporter_list,
		'Categorie_withCollec_list': Categorie_withCollec_list,
		'Collection_withCat_list': Collection_withCat_list,
    }
	return render(request, 'carre_app/index_marque.html', context)

def index_collection(request, collection_id):
	Categorie_list = Categorie.objects.all()
	Subcategorie_list = Subcategorie.objects.all()
	Collection_list = Collection.objects.all()
	Comporter_list = Comporter.objects.all()
	Categorie_withCollec_list = Categorie.objects.filter(id_categorie__in=Comporter_list)
	Collection_withCat_list = Collection.objects.filter(id_collection__in=Comporter_list)
	context = {
		'Categorie_list': Categorie_list,
		'Subcategorie_list': Subcategorie_list,
		'Collection_list': Collection_list,
		'Comporter_list': Comporter_list,
		'Categorie_withCollec_list': Categorie_withCollec_list,
		'Collection_withCat_list': Collection_withCat_list,
    }
	return render(request, 'carre_app/index_collection.html', context)

def index_adressendtel(request):
	Categorie_list = Categorie.objects.all()
	Subcategorie_list = Subcategorie.objects.all()
	Collection_list = Collection.objects.all()
	Comporter_list = Comporter.objects.all()
	Categorie_withCollec_list = Categorie.objects.filter(id_categorie__in=Comporter_list)
	Collection_withCat_list = Collection.objects.filter(id_collection__in=Comporter_list)
	context = {
		'Categorie_list': Categorie_list,
		'Subcategorie_list': Subcategorie_list,
		'Collection_list': Collection_list,
		'Comporter_list': Comporter_list,
		'Categorie_withCollec_list': Categorie_withCollec_list,
		'Collection_withCat_list': Collection_withCat_list,
    }
	return render(request, 'carre_app/index_adressendtel.html', context)

def index_categorie(request, categorie_id):
	the_Categorie = Categorie.objects.get(id_categorie = categorie_id)
	the_SubCategories = Subcategorie.objects.filter(id_categorie = categorie_id)
	Categorie_list = Categorie.objects.all()
	Subcategorie_list = Subcategorie.objects.all()
	Collection_list = Collection.objects.all()
	Comporter_list = Comporter.objects.all()
	Product_list = Product.objects.all()
	Categorie_withCollec_list = Categorie.objects.filter(id_categorie__in=Comporter_list)
	Collection_withCat_list = Collection.objects.filter(id_collection__in=Comporter_list)
	Comporter_list_forCat = Comporter.objects.filter(id_categorie=categorie_id)
	Collection_list_forCat = Collection.objects.filter(id_collection__in=Comporter_list_forCat)
	
	Product_bySub_list = Product.objects.filter(id_subcategorie__in=the_SubCategories)
	Collection_bySub_list = Collection.objects.filter(id_collection__in=Product_bySub_list)

	context = {
		'the_Categorie': the_Categorie,
		'the_SubCategories': the_SubCategories,
		'Categorie_list': Categorie_list,
		'Subcategorie_list': Subcategorie_list,
		'Collection_list': Collection_list,
		'Comporter_list': Comporter_list,
		'Categorie_withCollec_list': Categorie_withCollec_list,
		'Collection_withCat_list': Collection_withCat_list,
		'Collection_list_forCat': Collection_list_forCat,
		'Product_bySub_list': Product_bySub_list,
		'Collection_bySub_list': Collection_bySub_list,
    }
	return render(request, 'carre_app/index_categorie.html', context)

def index_collectionsalledebains(request):
	articles = [
		{'prefix': 'Arq', 'url': 'a_1-1', 'name': 'name_a_1-1', 'ref': 'ref_a_1-1'},
		{'prefix': 'Noble', 'url': 'a_1-2', 'name': 'name_a_1-2', 'ref': 'ref_a_1-2'},
		{'prefix': 'Eos', 'url': 'a_1-3', 'name': 'name_a_1-3', 'ref': 'ref_a_1-3'},
		{'prefix': 'Universal', 'url': 'a_1-4', 'name': 'name_a_1-4', 'ref': 'ref_a_1-4'},
		{'prefix': 'Klea', 'url': 'a_1-5', 'name': 'name_a_1-5', 'ref': 'ref_a_1-5'},
		{'prefix': 'Emma Square', 'url': 'a_1-6', 'name': 'name_a_1-6', 'ref': 'ref_a_1-6'},
		{'prefix': 'Emma', 'url': 'a_1-7', 'name': 'name_a_1-7', 'ref': 'ref_a_1-7'},
		{'prefix': 'Mid', 'url': 'a_1-8', 'name': 'name_a_1-8', 'ref': 'ref_a_1-8'},
		{'prefix': 'Smart', 'url': 'a_1-9', 'name': 'name_a_1-9', 'ref': 'ref_a_1-9'},
		{'prefix': 'Jazz', 'url': 'a_1-10', 'name': 'name_a_1-10', 'ref': 'ref_a_1-10'},
		{'prefix': 'Street Square', 'url': 'a_1-11', 'name': 'name_a_1-11', 'ref': 'ref_a_1-11'},
		{'prefix': 'Street', 'url': 'a_1-12', 'name': 'name_a_1-12', 'ref': 'ref_a_1-12'},
		{'prefix': 'Elia', 'url': 'a_1-13', 'name': 'name_a_1-13', 'ref': 'ref_a_1-13'},
		{'prefix': 'Arq', 'url': 'a_1-14', 'name': 'name_a_1-14', 'ref': 'ref_a_1-14'},
		{'prefix': 'Noble', 'url': 'a_1-15', 'name': 'name_a_1-15', 'ref': 'ref_a_1-15'},
		{'prefix': 'Eos', 'url': 'a_1-16', 'name': 'name_a_1-16', 'ref': 'ref_a_1-16'},
		{'prefix': 'Universal', 'url': 'a_1-17', 'name': 'name_a_1-17', 'ref': 'ref_a_1-17'},
		{'prefix': 'Klea', 'url': 'a_1-18', 'name': 'name_a_1-18', 'ref': 'ref_a_1-18'},
		{'prefix': 'Emma Square', 'url': 'a_1-19', 'name': 'name_a_1-19', 'ref': 'ref_a_1-19'},
		{'prefix': 'Emma', 'url': 'a_1-20', 'name': 'name_a_1-20', 'ref': 'ref_a_1-20'},
		{'prefix': 'Mid', 'url': 'a_1-21', 'name': 'name_a_1-21', 'ref': 'ref_a_1-21'},
		{'prefix': 'Smart', 'url': 'a_1-22', 'name': 'name_a_1-22', 'ref': 'ref_a_1-22'},
		{'prefix': 'Jazz', 'url': 'a_1-23', 'name': 'name_a_1-23', 'ref': 'ref_a_1-23'},
		{'prefix': 'Street Square', 'url': 'a_1-24', 'name': 'name_a_1-24', 'ref': 'ref_a_1-24'},
		{'prefix': 'Street', 'url': 'a_1-25', 'name': 'name_a_1-25', 'ref': 'ref_a_1-25'},
		{'prefix': 'Elia', 'url': 'a_1-26', 'name': 'name_a_1-26', 'ref': 'ref_a_1-26'},
	]

	Arq = []
	Noble = []
	Eos = []
	Universal = []
	Klea = []
	Emma_Square = []
	Emma = []
	Mid = []
	Smart = []
	Jazz = []
	Street_Square = []
	Street = []
	Elia = []

	for x in articles:
		if(x['prefix'] == 'Arq'):
			Arq.append(x)
		elif(x['prefix'] == 'Noble'):
			Noble.append(x)
		elif(x['prefix'] == 'Eos'):
			Eos.append(x)
		elif(x['prefix'] == 'Universal'):
			Universal.append(x)
		elif(x['prefix'] == 'Klea'):
			Klea.append(x)
		elif(x['prefix'] == 'Emma Square'):
			Emma_Square.append(x)
		elif(x['prefix'] == 'Emma'):
			Emma.append(x)
		elif(x['prefix'] == 'Mid'):
			Mid.append(x)
		elif(x['prefix'] == 'Smart'):
			Smart.append(x)
		elif(x['prefix'] == 'Jazz'):
			Jazz.append(x)
		elif(x['prefix'] == 'Street Square'):
			Street_Square.append(x)
		elif(x['prefix'] == 'Street'):
			Street.append(x)
		elif(x['prefix'] == 'Elia'):
			Elia.append(x)

	paginator_Arq = Paginator(Arq, 100)
	paginator_Noble = Paginator(Noble, 100)
	paginator_Eos = Paginator(Eos, 100)
	paginator_Universal = Paginator(Universal, 100)
	paginator_Klea = Paginator(Klea, 100)
	paginator_Emma_Square = Paginator(Emma_Square, 100)
	paginator_Emma = Paginator(Emma, 100)
	paginator_Mid = Paginator(Mid, 100)
	paginator_Smart = Paginator(Smart, 100)
	paginator_Jazz = Paginator(Jazz, 100)
	paginator_Street_Square = Paginator(Street_Square, 100)
	paginator_Street = Paginator(Street, 100)
	paginator_Elia = Paginator(Elia, 100)

	page = request.GET.get('page')
	try:
		Arq_list = paginator_Arq.page(page)
		Noble_list = paginator_Noble.page(page)
		Eos_list = paginator_Eos.page(page)
		Universal_list = paginator_Universal.page(page)
		Klea_list = paginator_Klea.page(page)
		Emma_Square_list = paginator_Emma_Square.page(page)
		Emma_list = paginator_Emma.page(page)
		Mid_list = paginator_Mid.page(page)
		Smart_list = paginator_Smart.page(page)
		Jazz_list = paginator_Jazz.page(page)
		Street_Square_list = paginator_Street_Square.page(page)
		Street_list = paginator_Street.page(page)
		Elia_list = paginator_Elia.page(page)
	except PageNotAnInteger:
		Arq_list = paginator_Arq.page(1)
		Noble_list = paginator_Noble.page(1)
		Eos_list = paginator_Eos.page(1)
		Universal_list = paginator_Universal.page(1)
		Klea_list = paginator_Klea.page(1)
		Emma_Square_list = paginator_Emma_Square.page(1)
		Emma_list = paginator_Emma.page(1)
		Mid_list = paginator_Mid.page(1)
		Smart_list = paginator_Smart.page(1)
		Jazz_list = paginator_Jazz.page(1)
		Street_Square_list = paginator_Street_Square.page(1)
		Street_list = paginator_Street.page(1)
		Elia_list = paginator_Elia.page(1)
	except EmptyPage:
		Arq_list = paginator_Arq.page(paginator_Arq.num_pages)
		Noble_list = paginator_Noble.page(paginator_Noble.num_pages)
		Eos_list = paginator_Eos.page(paginator_Eos.num_pages)
		Universal_list = paginator_Universal.page(paginator_Universal.num_pages)
		Klea_list = paginator_Klea.page(paginator_Klea.num_pages)
		Emma_Square_list = paginator_Emma_Square.page(paginator_Emma_Square.num_pages)
		Emma_list = paginator_Emma.page(paginator_Emma.num_pages)
		Mid_list = paginator_Mid.page(paginator_Mid.num_pages)
		Smart_list = paginator_Smart.page(paginator_Smart.num_pages)
		Jazz_list = paginator_Jazz.page(paginator_Jazz.num_pages)
		Street_Square_list = paginator_Street_Square.page(paginator_Street_Square.num_pages)
		Street_list = paginator_Street.page(paginator_Street.num_pages)
		Elia_list = paginator_Elia.page(paginator_Elia.num_pages)
	context = {
		'name': 'index_collectionsalledebains',
		'Arq_list': Arq_list,
		'Noble_list': Noble_list,
		'Eos_list': Eos_list,
		'Universal_list': Universal_list,
		'Klea_list': Klea_list,
		'Emma_Square_list': Emma_Square_list,
		'Emma_list': Emma_list,
		'Mid_list': Mid_list,
		'Smart_list': Smart_list,
		'Jazz_list': Jazz_list,
		'Street_Square_list': Street_Square_list,
		'Street_list': Street_list,
		'Elia_list': Elia_list,
	}
	return render(request, 'carre_app/index_collectionsalledebains.html', context)

def index_sanitaire(request):
	articles = [
		{'parent': 'Vasque', 'prefix': 'Metal-Line', 			'url': 'a_2-1-1-1', 	'name': 'name_a_2-1-1-1', 	'ref': 'ref_a_2-1-1-1'},
		{'parent': 'Vasque', 'prefix': 'Metal-Line', 			'url': 'a_2-1-1-2', 	'name': 'name_a_2-1-1-2', 	'ref': 'ref_a_2-1-1-2'},
		{'parent': 'Vasque', 'prefix': 'A Encastrer', 			'url': 'a_2-1-2-3', 	'name': 'name_a_2-1-2-3', 	'ref': 'ref_a_2-1-2-3'},
		{'parent': 'Vasque', 'prefix': 'A Encastrer', 			'url': 'a_2-1-2-4', 	'name': 'name_a_2-1-2-4', 	'ref': 'ref_a_2-1-2-4'},
		{'parent': 'Vasque', 'prefix': 'Sous-Plan', 			'url': 'a_2-1-3-5', 	'name': 'name_a_2-1-3-5', 	'ref': 'ref_a_2-1-3-5'},
		{'parent': 'Vasque', 'prefix': 'Sous-Plan', 			'url': 'a_2-1-3-6', 	'name': 'name_a_2-1-3-6', 	'ref': 'ref_a_2-1-3-6'},
		{'parent': 'Vasque', 'prefix': 'Semi-Encastrées', 		'url': 'a_2-1-4-7', 	'name': 'name_a_2-1-4-7', 	'ref': 'ref_a_2-1-4-7'},
		{'parent': 'Vasque', 'prefix': 'Semi-Encastrées', 		'url': 'a_2-1-4-8', 	'name': 'name_a_2-1-4-8', 	'ref': 'ref_a_2-1-4-8'},
		{'parent': 'Vasque', 'prefix': 'A Poser', 				'url': 'a_2-1-5-9', 	'name': 'name_a_2-1-5-9', 	'ref': 'ref_a_2-1-5-9'},
		{'parent': 'Vasque', 'prefix': 'A Poser', 				'url': 'a_2-1-5-10',	'name': 'name_a_2-1-5-10',	'ref': 'ref_a_2-1-5-10'},
		{'parent': 'Vasque', 'prefix': 'A Poser sur Meuble', 	'url': 'a_2-1-6-11',	'name': 'name_a_2-1-6-11', 	'ref': 'ref_a_2-1-6-11'},
		{'parent': 'Vasque', 'prefix': 'A Poser sur Meuble', 	'url': 'a_2-1-6-12',	'name': 'name_a_2-1-6-12', 	'ref': 'ref_a_2-1-6-12'},
		{'parent': 'Vasque', 'prefix': 'Lave-Mains', 			'url': 'a_2-1-7-13', 	'name': 'name_a_2-1-7-13', 	'ref': 'ref_a_2-1-7-13'},
		{'parent': 'Vasque', 'prefix': 'Lave-Mains', 			'url': 'a_2-1-7-14', 	'name': 'name_a_2-1-7-14', 	'ref': 'ref_a_2-1-7-14'},
		{'parent': 'Vasque', 'prefix': 'Muraux', 				'url': 'a_2-1-8-15', 	'name': 'name_a_2-1-8-15', 	'ref': 'ref_a_2-1-8-15'},
		{'parent': 'Vasque', 'prefix': 'Muraux', 				'url': 'a_2-1-8-16', 	'name': 'name_a_2-1-8-16', 	'ref': 'ref_a_2-1-8-16'},

		{'parent': 'Bidet', 'prefix': 'b-Arq', 					'url': 'a_2-2-1-17', 	'name': 'name_a_2-2-1-17', 	'ref': 'ref_a_2-2-1-17'},
		{'parent': 'Bidet', 'prefix': 'b-Arq', 					'url': 'a_2-2-1-18', 	'name': 'name_a_2-2-1-18', 	'ref': 'ref_a_2-2-1-18'},
		{'parent': 'Bidet', 'prefix': 'b-Noble', 					'url': 'a_2-2-2-19', 	'name': 'name_a_2-2-2-19', 	'ref': 'ref_a_2-2-2-19'},
		{'parent': 'Bidet', 'prefix': 'b-Noble', 					'url': 'a_2-2-2-20', 	'name': 'name_a_2-2-2-20', 	'ref': 'ref_a_2-2-2-20'},
		{'parent': 'Bidet', 'prefix': 'b-Eos', 					'url': 'a_2-2-3-21', 	'name': 'name_a_2-2-3-21', 	'ref': 'ref_a_2-2-3-21'},
		{'parent': 'Bidet', 'prefix': 'b-Eos', 					'url': 'a_2-2-3-22', 	'name': 'name_a_2-2-3-22', 	'ref': 'ref_a_2-2-3-22'},
		{'parent': 'Bidet', 'prefix': 'b-Universal', 				'url': 'a_2-2-4-23', 	'name': 'name_a_2-2-4-23', 	'ref': 'ref_a_2-2-4-23'},
		{'parent': 'Bidet', 'prefix': 'b-Universal', 				'url': 'a_2-2-4-24', 	'name': 'name_a_2-2-4-24', 	'ref': 'ref_a_2-2-4-24'},
		{'parent': 'Bidet', 'prefix': 'b-Klea', 					'url': 'a_2-2-5-25', 	'name': 'name_a_2-2-5-25', 	'ref': 'ref_a_2-2-5-25'},
		{'parent': 'Bidet', 'prefix': 'b-Klea', 					'url': 'a_2-2-5-26', 	'name': 'name_a_2-2-5-26', 	'ref': 'ref_a_2-2-5-26'},
		{'parent': 'Bidet', 'prefix': 'b-Emma Square', 			'url': 'a_2-2-6-27', 	'name': 'name_a_2-2-6-27', 	'ref': 'ref_a_2-2-6-27'},
		{'parent': 'Bidet', 'prefix': 'b-Emma Square', 			'url': 'a_2-2-6-28', 	'name': 'name_a_2-2-6-28', 	'ref': 'ref_a_2-2-6-28'},
		{'parent': 'Bidet', 'prefix': 'b-Emma', 					'url': 'a_2-2-7-29', 	'name': 'name_a_2-2-7-29', 	'ref': 'ref_a_2-2-7-29'},
		{'parent': 'Bidet', 'prefix': 'b-Emma', 					'url': 'a_2-2-7-30', 	'name': 'name_a_2-2-7-30', 	'ref': 'ref_a_2-2-7-30'},
		{'parent': 'Bidet', 'prefix': 'b-Mid', 					'url': 'a_2-2-8-31', 	'name': 'name_a_2-2-8-31', 	'ref': 'ref_a_2-2-8-31'},
		{'parent': 'Bidet', 'prefix': 'b-Mid', 					'url': 'a_2-2-8-32', 	'name': 'name_a_2-2-8-32', 	'ref': 'ref_a_2-2-8-32'},
		{'parent': 'Bidet', 'prefix': 'b-Smart', 					'url': 'a_2-2-9-33', 	'name': 'name_a_2-2-9-33', 	'ref': 'ref_a_2-2-9-33'},
		{'parent': 'Bidet', 'prefix': 'b-Smart', 					'url': 'a_2-2-9-34', 	'name': 'name_a_2-2-9-34', 	'ref': 'ref_a_2-2-9-34'},
		{'parent': 'Bidet', 'prefix': 'b-Jazz', 					'url': 'a_2-2-10-35', 	'name': 'name_a_2-2-10-35', 'ref': 'ref_a_2-2-10-35'},
		{'parent': 'Bidet', 'prefix': 'b-Jazz', 					'url': 'a_2-2-10-36', 	'name': 'name_a_2-2-10-36', 'ref': 'ref_a_2-2-10-36'},
		{'parent': 'Bidet', 'prefix': 'b-Street Square', 			'url': 'a_2-2-11-37', 	'name': 'name_a_2-2-11-37', 'ref': 'ref_a_2-2-11-37'},
		{'parent': 'Bidet', 'prefix': 'b-Street Square', 			'url': 'a_2-2-11-38', 	'name': 'name_a_2-2-11-38', 'ref': 'ref_a_2-2-11-38'},
		{'parent': 'Bidet', 'prefix': 'b-Street', 				'url': 'a_2-2-12-39', 	'name': 'name_a_2-2-12-39', 'ref': 'ref_a_2-2-12-39'},
		{'parent': 'Bidet', 'prefix': 'b-Street', 				'url': 'a_2-2-12-40', 	'name': 'name_a_2-2-12-40', 'ref': 'ref_a_2-2-12-40'},
		{'parent': 'Bidet', 'prefix': 'b-Elia', 					'url': 'a_2-2-13-41', 	'name': 'name_a_2-2-13-41', 'ref': 'ref_a_2-2-13-41'},
		{'parent': 'Bidet', 'prefix': 'b-Elia', 					'url': 'a_2-2-13-42', 	'name': 'name_a_2-2-13-42', 'ref': 'ref_a_2-2-13-42'},

		{'parent': 'Bloc WC', 'prefix': 'Arq', 					'url': 'a-2-3-1-17', 	'name': 'name_a-2-3-1-17', 	'ref': 'ref_a-2-3-1-17'},
		{'parent': 'Bloc WC', 'prefix': 'Arq', 					'url': 'a-2-3-1-18', 	'name': 'name_a-2-3-1-18', 	'ref': 'ref_a-2-3-1-18'},
		{'parent': 'Bloc WC', 'prefix': 'Noble', 				'url': 'a-2-3-2-19', 	'name': 'name_a-2-3-2-19', 	'ref': 'ref_a-2-3-2-19'},
		{'parent': 'Bloc WC', 'prefix': 'Noble', 				'url': 'a-2-3-2-20', 	'name': 'name_a-2-3-2-20', 	'ref': 'ref_a-2-3-2-20'},
		{'parent': 'Bloc WC', 'prefix': 'Eos', 					'url': 'a-2-3-3-21', 	'name': 'name_a-2-3-3-21', 	'ref': 'ref_a-2-3-3-21'},
		{'parent': 'Bloc WC', 'prefix': 'Eos', 					'url': 'a-2-3-3-22', 	'name': 'name_a-2-3-3-22', 	'ref': 'ref_a-2-3-3-22'},
		{'parent': 'Bloc WC', 'prefix': 'Universal', 			'url': 'a-2-3-4-23', 	'name': 'name_a-2-3-4-23', 	'ref': 'ref_a-2-3-4-23'},
		{'parent': 'Bloc WC', 'prefix': 'Universal', 			'url': 'a-2-3-4-24', 	'name': 'name_a-2-3-4-24', 	'ref': 'ref_a-2-3-4-24'},
		{'parent': 'Bloc WC', 'prefix': 'Klea', 				'url': 'a-2-3-5-25', 	'name': 'name_a-2-3-5-25', 	'ref': 'ref_a-2-3-5-25'},
		{'parent': 'Bloc WC', 'prefix': 'Klea', 				'url': 'a-2-3-5-26', 	'name': 'name_a-2-3-5-26', 	'ref': 'ref_a-2-3-5-26'},
		{'parent': 'Bloc WC', 'prefix': 'Emma Square', 			'url': 'a-2-3-6-27', 	'name': 'name_a-2-3-6-27', 	'ref': 'ref_a-2-3-6-27'},
		{'parent': 'Bloc WC', 'prefix': 'Emma Square', 			'url': 'a-2-3-6-28', 	'name': 'name_a-2-3-6-28', 	'ref': 'ref_a-2-3-6-28'},
		{'parent': 'Bloc WC', 'prefix': 'Emma', 				'url': 'a-2-3-7-29', 	'name': 'name_a-2-3-7-29', 	'ref': 'ref_a-2-3-7-29'},
		{'parent': 'Bloc WC', 'prefix': 'Emma', 				'url': 'a-2-3-7-30', 	'name': 'name_a-2-3-7-30', 	'ref': 'ref_a-2-3-7-30'},
		{'parent': 'Bloc WC', 'prefix': 'Mid', 					'url': 'a-2-3-8-31', 	'name': 'name_a-2-3-8-31', 	'ref': 'ref_a-2-3-8-31'},
		{'parent': 'Bloc WC', 'prefix': 'Mid', 					'url': 'a-2-3-8-32', 	'name': 'name_a-2-3-8-32', 	'ref': 'ref_a-2-3-8-32'},
		{'parent': 'Bloc WC', 'prefix': 'Smart', 				'url': 'a-2-3-9-33', 	'name': 'name_a-2-3-9-33', 	'ref': 'ref_a-2-3-9-33'},
		{'parent': 'Bloc WC', 'prefix': 'Smart', 				'url': 'a-2-3-9-34', 	'name': 'name_a-2-3-9-34', 	'ref': 'ref_a-2-3-9-34'},
		{'parent': 'Bloc WC', 'prefix': 'Jazz', 				'url': 'a-2-3-10-35', 	'name': 'name_a-2-3-10-35', 'ref': 'ref_a-2-3-10-35'},
		{'parent': 'Bloc WC', 'prefix': 'Jazz', 				'url': 'a-2-3-10-36', 	'name': 'name_a-2-3-10-36', 'ref': 'ref_a-2-3-10-36'},
		{'parent': 'Bloc WC', 'prefix': 'Street Square', 		'url': 'a-2-3-11-37', 	'name': 'name_a-2-3-11-37', 'ref': 'ref_a-2-3-11-37'},
		{'parent': 'Bloc WC', 'prefix': 'Street Square', 		'url': 'a-2-3-11-38', 	'name': 'name_a-2-3-11-38', 'ref': 'ref_a-2-3-11-38'},
		{'parent': 'Bloc WC', 'prefix': 'Street', 				'url': 'a-2-3-12-39', 	'name': 'name_a-2-3-12-39', 'ref': 'ref_a-2-3-12-39'},
		{'parent': 'Bloc WC', 'prefix': 'Street', 				'url': 'a-2-3-12-40', 	'name': 'name_a-2-3-12-40', 'ref': 'ref_a-2-3-12-40'},
		{'parent': 'Bloc WC', 'prefix': 'Elia', 				'url': 'a-2-3-13-41', 	'name': 'name_a-2-3-13-41', 'ref': 'ref_a-2-3-13-41'},
		{'parent': 'Bloc WC', 'prefix': 'Elia', 				'url': 'a-2-3-13-42', 	'name': 'name_a-2-3-13-42', 'ref': 'ref_a_2-3-13-42'},
	]

	Vasque_Metal_Line = []
	Vasque_A_Encastrer = []
	Vasque_Sous_Plan = []
	Vasque_Semi_Encastrées = []
	Vasque_A_Poser = []
	Vasque_A_Poser_sur_Meuble = []
	Vasque_Lave_Mains = []
	Vasque_Muraux = []

	Bidet_Arq = []
	Bidet_Noble = []
	Bidet_Eos = []
	Bidet_Universal = []
	Bidet_Klea = []
	Bidet_Emma_Square = []
	Bidet_Emma = []
	Bidet_Mid = []
	Bidet_Smart = []
	Bidet_Jazz = []
	Bidet_Street_Square = []
	Bidet_Street = []
	Bidet_Elia = []

	Bloc_WC_Arq = []
	Bloc_WC_Noble = []
	Bloc_WC_Eos = []
	Bloc_WC_Universal = []
	Bloc_WC_Klea = []
	Bloc_WC_Emma_Square = []
	Bloc_WC_Emma = []
	Bloc_WC_Mid = []
	Bloc_WC_Smart = []
	Bloc_WC_Jazz = []
	Bloc_WC_Street_Square = []
	Bloc_WC_Street = []
	Bloc_WC_Elia = []

	for x in articles:
		if(x['parent'] == 'Vasque'):
			if(x['prefix'] == 'Metal-Line'):
				Vasque_Metal_Line.append(x)
			elif(x['prefix'] == 'A Encastrer'):
				Vasque_A_Encastrer.append(x)
			elif(x['prefix'] == 'Sous-Plan'):
				Vasque_Sous_Plan.append(x)
			elif(x['prefix'] == 'Semi-Encastrées'):
				Vasque_Semi_Encastrées.append(x)
			elif(x['prefix'] == 'A Poser'):
				Vasque_A_Poser.append(x)
			elif(x['prefix'] == 'A Poser sur Meuble'):
				Vasque_A_Poser_sur_Meuble.append(x)
			elif(x['prefix'] == 'Lave-Mains'):
				Vasque_Lave_Mains.append(x)
			elif(x['prefix'] == 'Muraux'):
				Vasque_Muraux.append(x)
		elif(x['parent'] == 'Bidet'):
			if(x['prefix'] == 'b-Arq'):
				Bidet_Arq.append(x)
			elif(x['prefix'] == 'b-Noble'):
				Bidet_Noble.append(x)
			elif(x['prefix'] == 'b-Eos'):
				Bidet_Eos.append(x)
			elif(x['prefix'] == 'b-Universal'):
				Bidet_Universal.append(x)
			elif(x['prefix'] == 'b-Klea'):
				Bidet_Klea.append(x)
			elif(x['prefix'] == 'b-Emma Square'):
				Bidet_Emma_Square.append(x)
			elif(x['prefix'] == 'b-Emma'):
				Bidet_Emma.append(x)
			elif(x['prefix'] == 'b-Mid'):
				Bidet_Mid.append(x)
			elif(x['prefix'] == 'b-Smart'):
				Bidet_Smart.append(x)
			elif(x['prefix'] == 'b-Jazz'):
				Bidet_Jazz.append(x)
			elif(x['prefix'] == 'b-Street Square'):
				Bidet_Street_Square.append(x)
			elif(x['prefix'] == 'b-Street'):
				Bidet_Street.append(x)
			elif(x['prefix'] == 'b-Elia'):
				Bidet_Elia.append(x)
		elif(x['parent'] == 'Bloc WC'):
			if(x['prefix'] == 'Arq'):
				Bloc_WC_Arq.append(x)
			elif(x['prefix'] == 'Noble'):
				Bloc_WC_Noble.append(x)
			elif(x['prefix'] == 'Eos'):
				Bloc_WC_Eos.append(x)
			elif(x['prefix'] == 'Universal'):
				Bloc_WC_Universal.append(x)
			elif(x['prefix'] == 'Klea'):
				Bloc_WC_Klea.append(x)
			elif(x['prefix'] == 'Emma Square'):
				Bloc_WC_Emma_Square.append(x)
			elif(x['prefix'] == 'Emma'):
				Bloc_WC_Emma.append(x)
			elif(x['prefix'] == 'Mid'):
				Bloc_WC_Mid.append(x)
			elif(x['prefix'] == 'Smart'):
				Bloc_WC_Smart.append(x)
			elif(x['prefix'] == 'Jazz'):
				Bloc_WC_Jazz.append(x)
			elif(x['prefix'] == 'Street Square'):
				Bloc_WC_Street_Square.append(x)
			elif(x['prefix'] == 'Street'):
				Bloc_WC_Street.append(x)
			elif(x['prefix'] == 'Elia'):
				Bloc_WC_Elia.append(x)

	paginator_Vasque_Metal_Line = Paginator(Vasque_Metal_Line, 100)
	paginator_Vasque_A_Encastrer = Paginator(Vasque_A_Encastrer, 100)
	paginator_Vasque_Sous_Plan = Paginator(Vasque_Sous_Plan, 100)
	paginator_Vasque_Semi_Encastrées = Paginator(Vasque_Semi_Encastrées, 100)
	paginator_Vasque_A_Poser = Paginator(Vasque_A_Poser, 100)
	paginator_Vasque_A_Poser_sur_Meuble = Paginator(Vasque_A_Poser_sur_Meuble, 100)
	paginator_Vasque_Lave_Mains = Paginator(Vasque_Lave_Mains, 100)
	paginator_Vasque_Muraux = Paginator(Vasque_Muraux, 100)
	paginator_Bidet_Arq = Paginator(Bidet_Arq, 100)
	paginator_Bidet_Noble = Paginator(Bidet_Noble, 100)
	paginator_Bidet_Eos = Paginator(Bidet_Eos, 100)
	paginator_Bidet_Universal = Paginator(Bidet_Universal, 100)
	paginator_Bidet_Klea = Paginator(Bidet_Klea, 100)
	paginator_Bidet_Emma_Square = Paginator(Bidet_Emma_Square, 100)
	paginator_Bidet_Emma = Paginator(Bidet_Emma, 100)
	paginator_Bidet_Mid = Paginator(Bidet_Mid, 100)
	paginator_Bidet_Smart = Paginator(Bidet_Smart, 100)
	paginator_Bidet_Jazz = Paginator(Bidet_Jazz, 100)
	paginator_Bidet_Street_Square = Paginator(Bidet_Street_Square, 100)
	paginator_Bidet_Street = Paginator(Bidet_Street, 100)
	paginator_Bidet_Elia = Paginator(Bidet_Elia, 100)
	paginator_Bloc_WC_Arq = Paginator(Bloc_WC_Arq, 100)
	paginator_Bloc_WC_Eos = Paginator(Bloc_WC_Eos, 100)
	paginator_Bloc_WC_Universal = Paginator(Bloc_WC_Universal, 100)
	paginator_Bloc_WC_Klea = Paginator(Bloc_WC_Klea, 100)
	paginator_Bloc_WC_Emma_Square = Paginator(Bloc_WC_Emma_Square, 100)
	paginator_Bloc_WC_Emma = Paginator(Bloc_WC_Emma, 100)
	paginator_Bloc_WC_Mid = Paginator(Bloc_WC_Mid, 100)
	paginator_Bloc_WC_Smart = Paginator(Bloc_WC_Smart, 100)
	paginator_Bloc_WC_Jazz = Paginator(Bloc_WC_Jazz, 100)
	paginator_Bloc_WC_Street_Square = Paginator(Bloc_WC_Street_Square, 100)
	paginator_Bloc_WC_Street = Paginator(Bloc_WC_Street, 100)
	paginator_Bloc_WC_Elia = Paginator(Bloc_WC_Elia, 100)

	page = request.GET.get('page')
	try:
		Vasque_Metal_Line_list = paginator_Vasque_Metal_Line.page(page)
		Vasque_A_Encastrer_list = paginator_Vasque_A_Encastrer.page(page)
		Vasque_Sous_Plan_list = paginator_Vasque_Sous_Plan.page(page)
		Vasque_Semi_Encastrées_list = paginator_Vasque_Semi_Encastrées.page(page)
		Vasque_A_Poser_list = paginator_Vasque_A_Poser.page(page)
		Vasque_A_Poser_sur_Meuble_list = paginator_Vasque_A_Poser_sur_Meuble.page(page)
		Vasque_Lave_Mains_list = paginator_Vasque_Lave_Mains.page(page)
		Vasque_Muraux_list = paginator_Vasque_Muraux.page(page)
		Bidet_Arq_list = paginator_Bidet_Arq.page(page)
		Bidet_Noble_list = paginator_Bidet_Noble.page(page)
		Bidet_Eos_list = paginator_Bidet_Eos.page(page)
		Bidet_Universal_list = paginator_Bidet_Universal.page(page)
		Bidet_Klea_list = paginator_Bidet_Klea.page(page)
		Bidet_Emma_Square_list = paginator_Bidet_Emma_Square.page(page)
		Bidet_Emma_list = paginator_Bidet_Emma.page(page)
		Bidet_Mid_list = paginator_Bidet_Mid.page(page)
		Bidet_Smart_list = paginator_Bidet_Smart.page(page)
		Bidet_Jazz_list = paginator_Bidet_Jazz.page(page)
		Bidet_Street_Square_list = paginator_Bidet_Street_Square.page(page)
		Bidet_Street_list = paginator_Bidet_Street.page(page)
		Bidet_Elia_list = paginator_Bidet_Elia.page(page)
		Bloc_WC_Arq_list = paginator_Bloc_WC_Arq.page(page)
		Bloc_WC_Eos_list = paginator_Bloc_WC_Eos.page(page)
		Bloc_WC_Universal_list = paginator_Bloc_WC_Universal.page(page)
		Bloc_WC_Klea_list = paginator_Bloc_WC_Klea.page(page)
		Bloc_WC_Emma_Square_list = paginator_Bloc_WC_Emma_Square.page(page)
		Bloc_WC_Emma_list = paginator_Bloc_WC_Emma.page(page)
		Bloc_WC_Mid_list = paginator_Bloc_WC_Mid.page(page)
		Bloc_WC_Smart_list = paginator_Bloc_WC_Smart.page(page)
		Bloc_WC_Jazz_list = paginator_Bloc_WC_Jazz.page(page)
		Bloc_WC_Street_Square_list = paginator_Bloc_WC_Street_Square.page(page)
		Bloc_WC_Street_list = paginator_Bloc_WC_Street.page(page)
		Bloc_WC_Elia_list = paginator_Bloc_WC_Elia.page(page)
	except PageNotAnInteger:
		Vasque_Metal_Line_list = paginator_Vasque_Metal_Line.page(1)
		Vasque_A_Encastrer_list = paginator_Vasque_A_Encastrer.page(1)
		Vasque_Sous_Plan_list = paginator_Vasque_Sous_Plan.page(1)
		Vasque_Semi_Encastrées_list = paginator_Vasque_Semi_Encastrées.page(1)
		Vasque_A_Poser_list = paginator_Vasque_A_Poser.page(1)
		Vasque_A_Poser_sur_Meuble_list = paginator_Vasque_A_Poser_sur_Meuble.page(1)
		Vasque_Lave_Mains_list = paginator_Vasque_Lave_Mains.page(1)
		Vasque_Muraux_list = paginator_Vasque_Muraux.page(1)
		Bidet_Arq_list = paginator_Bidet_Arq.page(1)
		Bidet_Noble_list = paginator_Bidet_Noble.page(1)
		Bidet_Eos_list = paginator_Bidet_Eos.page(1)
		Bidet_Universal_list = paginator_Bidet_Universal.page(1)
		Bidet_Klea_list = paginator_Bidet_Klea.page(1)
		Bidet_Emma_Square_list = paginator_Bidet_Emma_Square.page(1)
		Bidet_Emma_list = paginator_Bidet_Emma.page(1)
		Bidet_Mid_list = paginator_Bidet_Mid.page(1)
		Bidet_Smart_list = paginator_Bidet_Smart.page(1)
		Bidet_Jazz_list = paginator_Bidet_Jazz.page(1)
		Bidet_Street_Square_list = paginator_Bidet_Street_Square.page(1)
		Bidet_Street_list = paginator_Bidet_Street.page(1)
		Bidet_Elia_list = paginator_Bidet_Elia.page(1)
		Bloc_WC_Arq_list = paginator_Bloc_WC_Arq.page(1)
		Bloc_WC_Eos_list = paginator_Bloc_WC_Eos.page(1)
		Bloc_WC_Universal_list = paginator_Bloc_WC_Universal.page(1)
		Bloc_WC_Klea_list = paginator_Bloc_WC_Klea.page(1)
		Bloc_WC_Emma_Square_list = paginator_Bloc_WC_Emma_Square.page(1)
		Bloc_WC_Emma_list = paginator_Bloc_WC_Emma.page(1)
		Bloc_WC_Mid_list = paginator_Bloc_WC_Mid.page(1)
		Bloc_WC_Smart_list = paginator_Bloc_WC_Smart.page(1)
		Bloc_WC_Jazz_list = paginator_Bloc_WC_Jazz.page(1)
		Bloc_WC_Street_Square_list = paginator_Bloc_WC_Street_Square.page(1)
		Bloc_WC_Street_list = paginator_Bloc_WC_Street.page(1)
		Bloc_WC_Elia_list = paginator_Bloc_WC_Elia.page(1)
	except EmptyPage:
		Vasque_Metal_Line_list = paginator_Vasque_Metal_Line.page(paginator_Vasque_Metal_Line.num_pages)
		Vasque_A_Encastrer_list = paginator_Vasque_A_Encastrer.page(paginator_Vasque_A_Encastrer.num_pages)
		Vasque_Sous_Plan_list = paginator_Vasque_Sous_Plan.page(paginator_Vasque_Sous_Plan.num_pages)
		Vasque_Semi_Encastrées_list = paginator_Vasque_Semi_Encastrées.page(paginator_Vasque_Semi_Encastrées.num_pages)
		Vasque_A_Poser_list = paginator_Vasque_A_Poser.page(paginator_Vasque_A_Poser.num_pages)
		Vasque_A_Poser_sur_Meuble_list = paginator_Vasque_A_Poser_sur_Meuble.page(paginator_Vasque_A_Poser_sur_Meuble.num_pages)
		Vasque_Lave_Mains_list = paginator_Vasque_Lave_Mains.page(paginator_Vasque_Lave_Mains.num_pages)
		Vasque_Muraux_list = paginator_Vasque_Muraux.page(paginator_Vasque_Muraux.num_pages)
		Bidet_Arq_list = paginator_Bidet_Arq.page(paginator_Bidet_Arq.num_pages)
		Bidet_Noble_list = paginator_Bidet_Noble.page(paginator_Bidet_Noble.num_pages)
		Bidet_Eos_list = paginator_Bidet_Eos.page(paginator_Bidet_Eos.num_pages)
		Bidet_Universal_list = paginator_Bidet_Universal.page(paginator_Bidet_Universal.num_pages)
		Bidet_Klea_list = paginator_Bidet_Klea.page(paginator_Bidet_Klea.num_pages)
		Bidet_Emma_Square_list = paginator_Bidet_Emma_Square.page(paginator_Bidet_Emma_Square.num_pages)
		Bidet_Emma_list = paginator_Bidet_Emma.page(paginator_Bidet_Emma.num_pages)
		Bidet_Mid_list = paginator_Bidet_Mid.page(paginator_Bidet_Mid.num_pages)
		Bidet_Smart_list = paginator_Bidet_Smart.page(paginator_Bidet_Smart.num_pages)
		Bidet_Jazz_list = paginator_Bidet_Jazz.page(paginator_Bidet_Jazz.num_pages)
		Bidet_Street_Square_list = paginator_Bidet_Street_Square.page(paginator_Bidet_Street_Square.num_pages)
		Bidet_Street_list = paginator_Bidet_Street.page(paginator_Bidet_Street.num_pages)
		Bidet_Elia_list = paginator_Bidet_Elia.page(paginator_Bidet_Elia.num_pages)
		Bloc_WC_Arq_list = paginator_Bloc_WC_Arq.page(paginator_Bloc_WC_Arq.num_pages)
		Bloc_WC_Eos_list = paginator_Bloc_WC_Eos.page(paginator_Bloc_WC_Eos.num_pages)
		Bloc_WC_Universal_list = paginator_Bloc_WC_Universal.page(paginator_Bloc_WC_Universal.num_pages)
		Bloc_WC_Klea_list = paginator_Bloc_WC_Klea.page(paginator_Bloc_WC_Klea.num_pages)
		Bloc_WC_Emma_Square_list = paginator_Bloc_WC_Emma_Square.page(paginator_Bloc_WC_Emma_Square.num_pages)
		Bloc_WC_Emma_list = paginator_Bloc_WC_Emma.page(paginator_Bloc_WC_Emma.num_pages)
		Bloc_WC_Mid_list = paginator_Bloc_WC_Mid.page(paginator_Bloc_WC_Mid.num_pages)
		Bloc_WC_Smart_list = paginator_Bloc_WC_Smart.page(paginator_Bloc_WC_Smart.num_pages)
		Bloc_WC_Jazz_list = paginator_Bloc_WC_Jazz.page(paginator_Bloc_WC_Jazz.num_pages)
		Bloc_WC_Street_Square_list = paginator_Bloc_WC_Street_Square.page(paginator_Bloc_WC_Street_Square.num_pages)
		Bloc_WC_Street_list = paginator_Bloc_WC_Street.page(paginator_Bloc_WC_Street.num_pages)
		Bloc_WC_Elia_list = paginator_Bloc_WC_Elia.page(paginator_Bloc_WC_Elia.num_pages)

	final_articles = {
		'Vasque_Metal_Line_list': Vasque_Metal_Line_list,
		'Vasque_A_Encastrer_list': Vasque_A_Encastrer_list,
		'Vasque_Sous_Plan_list': Vasque_Sous_Plan_list,
		'Vasque_Semi_Encastrées_list': Vasque_Semi_Encastrées_list,
		'Vasque_A_Poser_list': Vasque_A_Poser_list,
		'Vasque_A_Poser_sur_Meuble_list': Vasque_A_Poser_sur_Meuble_list,
		'Vasque_Lave_Mains_list': Vasque_Lave_Mains_list,
		'Vasque_Muraux_list': Vasque_Muraux_list,
		'Bidet_Arq_list': Bidet_Arq_list,
		'Bidet_Noble_list': Bidet_Noble_list,
		'Bidet_Eos_list': Bidet_Eos_list,
		'Bidet_Universal_list': Bidet_Universal_list,
		'Bidet_Klea_list': Bidet_Klea_list,
		'Bidet_Emma_Square_list': Bidet_Emma_Square_list,
		'Bidet_Emma_list': Bidet_Emma_list,
		'Bidet_Mid_list': Bidet_Mid_list,
		'Bidet_Smart_list': Bidet_Smart_list,
		'Bidet_Jazz_list': Bidet_Jazz_list,
		'Bidet_Street_Square_list': Bidet_Street_Square_list,
		'Bidet_Street_list': Bidet_Street_list,
		'Bidet_Elia_list': Bidet_Elia_list,
		'Bloc_WC_Arq_list': Bloc_WC_Arq_list,
		'Bloc_WC_Eos_list': Bloc_WC_Eos_list,
		'Bloc_WC_Universal_list': Bloc_WC_Universal_list,
		'Bloc_WC_Klea_list': Bloc_WC_Klea_list,
		'Bloc_WC_Emma_Square_list': Bloc_WC_Emma_Square_list,
		'Bloc_WC_Emma_list': Bloc_WC_Emma_list,
		'Bloc_WC_Mid_list': Bloc_WC_Mid_list,
		'Bloc_WC_Smart_list': Bloc_WC_Smart_list,
		'Bloc_WC_Jazz_list': Bloc_WC_Jazz_list,
		'Bloc_WC_Street_Square_list': Bloc_WC_Street_Square_list,
		'Bloc_WC_Street_list': Bloc_WC_Street_list,
		'Bloc_WC_Elia_list': Bloc_WC_Elia_list,
	}

	vasqueitems = 0
	bidetitems = 0
	blocitems = 0

	for x in articles:
		if(x['parent'] == 'Vasque'):
			vasqueitems += 1
		elif(x['parent'] == 'Bidet'):
			bidetitems += 1
		elif(x['parent'] == 'Bloc WC'):
			blocitems += 1

	result = {}
	for k in articles:
		if 'prefix' in k and 'parent' in k:
			result[k['prefix']] = result.get(k['prefix'], 0) + 1

	indexing_vasque = [str(vasqueitems), 'Metal-Line', 'A Encastrer', 'Sous-Plan', 'Semi-Encastrées', 'A Poser', 'A Poser sur Meuble', 'Lave-Mains', 'Muraux']
	indexing_bidet = [str(bidetitems), 'Arq', 'Noble', 'Eos', 'Universal', 'Klea', 'Emma Square', 'Emma', 'Mid', 'Smart', 'Jazz', 'Street Square', 'Street', 'Elia']
	indexing_bloc = [str(blocitems), 'Arq', 'Noble', 'Eos', 'Universal', 'Klea', 'Emma Square', 'Emma', 'Mid', 'Smart', 'Jazz', 'Street Square', 'Street', 'Elia']
	indexing_all = {
		'Vasque': indexing_vasque,
		'Bidet' : indexing_bidet,
		'Bloc_WC': indexing_bloc,
	}

	context = {
		'final_articles': final_articles,
		'vasqueitems': vasqueitems,
		'bidetitems': bidetitems,
		'blocitems': blocitems,
		'indexing_all': indexing_all,
		'result': result,
	}
	return render(request, 'carre_app/index_sanitaire.html', context)

def index_baignoiresetreceveurs(request):
	articles = [
		{'prefix': 'Baignoires', 'url': 'a_2-1', 'name': 'name_a_2-1', 'ref': 'ref_a_2-1'},
		{'prefix': 'Baignoires', 'url': 'a_2-2', 'name': 'name_a_2-2', 'ref': 'ref_a_2-2'},
		{'prefix': 'Baignoires', 'url': 'a_2-3', 'name': 'name_a_2-3', 'ref': 'ref_a_2-3'},
		{'prefix': 'Baignoires', 'url': 'a_2-4', 'name': 'name_a_2-4', 'ref': 'ref_a_2-4'},
		{'prefix': 'Baignoires', 'url': 'a_2-5', 'name': 'name_a_2-5', 'ref': 'ref_a_2-5'},
		{'prefix': 'Baignoires', 'url': 'a_2-6', 'name': 'name_a_2-6', 'ref': 'ref_a_2-6'},
		{'prefix': 'Baignoires', 'url': 'a_2-7', 'name': 'name_a_2-7', 'ref': 'ref_a_2-7'},
		{'prefix': 'Baignoires', 'url': 'a_2-8', 'name': 'name_a_2-8', 'ref': 'ref_a_2-8'},
		{'prefix': 'Receveurs', 'url': 'a_2-9', 'name': 'name_a_2-9', 'ref': 'ref_a_2-9'},
		{'prefix': 'Receveurs', 'url': 'a_2-10', 'name': 'name_a_2-10', 'ref': 'ref_a_2-10'},
		{'prefix': 'Receveurs', 'url': 'a_2-11', 'name': 'name_a_2-11', 'ref': 'ref_a_2-11'},
		{'prefix': 'Receveurs', 'url': 'a_2-12', 'name': 'name_a_2-12', 'ref': 'ref_a_2-12'},
		{'prefix': 'Receveurs', 'url': 'a_2-13', 'name': 'name_a_2-13', 'ref': 'ref_a_2-13'},
		{'prefix': 'Receveurs', 'url': 'a_2-14', 'name': 'name_a_2-14', 'ref': 'ref_a_2-14'},
	]

	Baignoires = []
	Receveurs = []

	for x in articles:
		if(x['prefix'] == 'Baignoires'):
			Baignoires.append(x)
		elif(x['prefix'] == 'Receveurs'):
			Receveurs.append(x)

	paginator_Baignoires = Paginator(Baignoires, 100)
	paginator_Receveurs = Paginator(Receveurs, 100)

	page = request.GET.get('page')
	try:
		Baignoires_list = paginator_Baignoires.page(page)
		Receveurs_list = paginator_Receveurs.page(page)
	except PageNotAnInteger:
		Baignoires_list = paginator_Baignoires.page(1)
		Receveurs_list = paginator_Receveurs.page(1)
	except EmptyPage:
		Baignoires_list = paginator_Baignoires.page(paginator_Baignoires.num_pages)
		Receveurs_list = paginator_Receveurs.page(paginator_Receveurs.num_pages)
	context = {
		'name': 'index_baignoiresetreceveurs',
		'Baignoires_list': Baignoires_list,
		'Receveurs_list': Receveurs_list,
	}
	return render(request, 'carre_app/index_baignoiresetreceveurs.html', context)

def index_miroirs(request):
	articles = [
		{'prefix': 'Standard', 'url': 'a_3-1', 'name': 'name_a_3-1', 'ref': 'ref_a_3-1'},
		{'prefix': 'Avec Lampe', 'url': 'a_3-2', 'name': 'name_a_3-2', 'ref': 'ref_a_3-2'},
		{'prefix': 'Avec LED', 'url': 'a_3-3', 'name': 'name_a_3-3', 'ref': 'ref_a_3-3'},
		{'prefix': 'Ovale', 'url': 'a_3-4', 'name': 'name_a_3-4', 'ref': 'ref_a_3-4'},
		{'prefix': 'Carré', 'url': 'a_3-5', 'name': 'name_a_3-5', 'ref': 'ref_a_3-5'},
		{'prefix': 'Standard', 'url': 'a_3-6', 'name': 'name_a_3-6', 'ref': 'ref_a_3-6'},
		{'prefix': 'Avec Lampe', 'url': 'a_3-7', 'name': 'name_a_3-7', 'ref': 'ref_a_3-7'},
		{'prefix': 'Avec LED', 'url': 'a_3-8', 'name': 'name_a_3-8', 'ref': 'ref_a_3-8'},
		{'prefix': 'Ovale', 'url': 'a_3-9', 'name': 'name_a_3-9', 'ref': 'ref_a_3-9'},
		{'prefix': 'Carré', 'url': 'a_3-10', 'name': 'name_a_3-10', 'ref': 'ref_a_3-10'},
		{'prefix': 'Standard', 'url': 'a_3-11', 'name': 'name_a_3-11', 'ref': 'ref_a_3-11'},
		{'prefix': 'Avec Lampe', 'url': 'a_3-12', 'name': 'name_a_3-12', 'ref': 'ref_a_3-12'},
		{'prefix': 'Avec LED', 'url': 'a_3-13', 'name': 'name_a_3-13', 'ref': 'ref_a_3-13'},
		{'prefix': 'Ovale', 'url': 'a_3-14', 'name': 'name_a_3-14', 'ref': 'ref_a_3-14'},
		{'prefix': 'Carré', 'url': 'a_3-15', 'name': 'name_a_3-15', 'ref': 'ref_a_3-15'},
		{'prefix': 'Standard', 'url': 'a_3-16', 'name': 'name_a_3-16', 'ref': 'ref_a_3-16'},
		{'prefix': 'Avec Lampe', 'url': 'a_3-17', 'name': 'name_a_3-17', 'ref': 'ref_a_3-17'},
		{'prefix': 'Avec LED', 'url': 'a_3-18', 'name': 'name_a_3-18', 'ref': 'ref_a_3-18'},
	]

	Standard = []
	Avec_Lampe = []
	Avec_LED = []
	Ovale = []
	Carre = []

	for x in articles:
		if(x['prefix'] == 'Standard'):
			Standard.append(x)
		elif(x['prefix'] == 'Avec Lampe'):
			Avec_Lampe.append(x)
		elif(x['prefix'] == 'Avec LED'):
			Avec_LED.append(x)
		elif(x['prefix'] == 'Ovale'):
			Ovale.append(x)
		elif(x['prefix'] == 'Carré'):
			Carre.append(x)

	paginator_Standard = Paginator(Standard, 100)
	paginator_Avec_Lampe = Paginator(Avec_Lampe, 100)
	paginator_Avec_LED = Paginator(Avec_LED, 100)
	paginator_Ovale = Paginator(Ovale, 100)
	paginator_Carre = Paginator(Carre, 100)

	page = request.GET.get('page')
	try:
		Standard_list = paginator_Standard.page(page)
		Avec_Lampe_list = paginator_Avec_Lampe.page(page)
		Avec_LED_list = paginator_Avec_LED.page(page)
		Ovale_list = paginator_Ovale.page(page)
		Carre_list = paginator_Carre.page(page)
	except PageNotAnInteger:
		Standard_list = paginator_Standard.page(1)
		Avec_Lampe_list = paginator_Avec_Lampe.page(1)
		Avec_LED_list = paginator_Avec_LED.page(1)
		Ovale_list = paginator_Ovale.page(1)
		Carre_list = paginator_Carre.page(1)
	except EmptyPage:
		Standard_list = paginator_Standard.page(paginator_Standard.num_pages)
		Avec_Lampe_list = paginator_Avec_Lampe.page(paginator_Avec_Lampe.num_pages)
		Avec_LED_list = paginator_Avec_LED.page(paginator_Avec_LED.num_pages)
		Ovale_list = paginator_Ovale.page(paginator_Ovale.num_pages)
		Carre_list = paginator_Carre.page(paginator_Carre.num_pages)
	context = {
		'name': 'index_miroirs',
		'Standard_list': Standard_list,
		'Avec_Lampe_list': Avec_Lampe_list,
		'Avec_LED_list': Avec_LED_list,
		'Ovale_list': Ovale_list,
		'Carre_list': Carre_list,
	}
	return render(request, 'carre_app/index_miroirs.html', context)

def index_meubles(request):
	articles = [
		{'prefix': 'DINAR', 'url': 'a_4-1', 'name': 'name_a_4-1', 'ref': 'ref_a_4-1'},
		{'prefix': 'LUNA', 'url': 'a_4-2', 'name': 'name_a_4-2', 'ref': 'ref_a_4-2'},
		{'prefix': 'MARMARA', 'url': 'a_4-3', 'name': 'name_a_4-3', 'ref': 'ref_a_4-3'},
		{'prefix': 'MARS', 'url': 'a_4-4', 'name': 'name_a_4-4', 'ref': 'ref_a_4-4'},
		{'prefix': 'MILAS', 'url': 'a_4-5', 'name': 'name_a_4-5', 'ref': 'ref_a_4-5'},
		{'prefix': 'SAMBA', 'url': 'a_4-6', 'name': 'name_a_4-6', 'ref': 'ref_a_4-6'},
		{'prefix': 'SOMA', 'url': 'a_4-7', 'name': 'name_a_4-7', 'ref': 'ref_a_4-7'},
		{'prefix': 'VALS', 'url': 'a_4-8', 'name': 'name_a_4-8', 'ref': 'ref_a_4-8'},
	]

	DINAR = []
	LUNA = []
	MARMARA = []
	MARS = []
	MILAS = []
	SAMBA = []
	SOMA = []
	VALS = []

	for x in articles:
		if(x['prefix'] == 'DINAR'):
			DINAR.append(x)
		elif(x['prefix'] == 'LUNA'):
			LUNA.append(x)
		elif(x['prefix'] == 'MARMARA'):
			MARMARA.append(x)
		elif(x['prefix'] == 'MARS'):
			MARS.append(x)
		elif(x['prefix'] == 'MILAS'):
			MILAS.append(x)
		elif(x['prefix'] == 'SAMBA'):
			SAMBA.append(x)
		elif(x['prefix'] == 'SOMA'):
			SOMA.append(x)
		elif(x['prefix'] == 'VALS'):
			VALS.append(x)

	paginator_DINAR = Paginator(DINAR, 100)
	paginator_LUNA = Paginator(LUNA, 100)
	paginator_MARMARA = Paginator(MARMARA, 100)
	paginator_MARS = Paginator(MARS, 100)
	paginator_MILAS = Paginator(MILAS, 100)
	paginator_SAMBA = Paginator(SAMBA, 100)
	paginator_SOMA = Paginator(SOMA, 100)
	paginator_VALS = Paginator(VALS, 100)

	page = request.GET.get('page')
	try:
		DINAR_list = paginator_DINAR.page(page)
		LUNA_list = paginator_LUNA.page(page)
		MARMARA_list = paginator_MARMARA.page(page)
		MARS_list = paginator_MARS.page(page)
		MILAS_list = paginator_MILAS.page(page)
		SAMBA_list = paginator_SAMBA.page(page)
		SOMA_list = paginator_SOMA.page(page)
		VALS_list = paginator_VALS.page(page)
	except PageNotAnInteger:
		DINAR_list = paginator_DINAR.page(1)
		LUNA_list = paginator_LUNA.page(1)
		MARMARA_list = paginator_MARMARA.page(1)
		MARS_list = paginator_MARS.page(1)
		MILAS_list = paginator_MILAS.page(1)
		SAMBA_list = paginator_SAMBA.page(1)
		SOMA_list = paginator_SOMA.page(1)
		VALS_list = paginator_VALS.page(1)
	except EmptyPage:
		DINAR_list = paginator_DINAR.page(paginator_DINAR.num_pages)
		LUNA_list = paginator_LUNA.page(paginator_LUNA.num_pages)
		MARMARA_list = paginator_MARMARA.page(paginator_MARMARA.num_pages)
		MARS_list = paginator_MARS.page(paginator_MARS.num_pages)
		MILAS_list = paginator_MILAS.page(paginator_MILAS.num_pages)
		SAMBA_list = paginator_SAMBA.page(paginator_SAMBA.num_pages)
		SOMA_list = paginator_SOMA.page(paginator_SOMA.num_pages)
		VALS_list = paginator_VALS.page(paginator_VALS.num_pages)
	context = {
		'name': 'index_meubles',
		'DINAR_list': DINAR_list,
		'LUNA_list': LUNA_list,
		'MARMARA_list': MARMARA_list,
		'MARS_list': MARS_list,
		'MILAS_list': MILAS_list,
		'SAMBA_list': SAMBA_list,
		'SOMA_list': SOMA_list,
		'VALS_list': VALS_list,
	}
	return render(request, 'carre_app/index_meubles.html', context)

def index_eviers(request):
	articles = [
		{'prefix': 'Simple', 'url': 'a_5-1', 'name': 'name_a_5-1', 'ref': 'ref_a_5-1'},
		{'prefix': 'Simple', 'url': 'a_5-2', 'name': 'name_a_5-2', 'ref': 'ref_a_5-2'},
		{'prefix': 'Simple', 'url': 'a_5-3', 'name': 'name_a_5-3', 'ref': 'ref_a_5-3'},
		{'prefix': 'Circulaire', 'url': 'a_5-4', 'name': 'name_a_5-4', 'ref': 'ref_a_5-4'},
		{'prefix': 'Circulaire', 'url': 'a_5-5', 'name': 'name_a_5-5', 'ref': 'ref_a_5-5'},
		{'prefix': 'Circulaire', 'url': 'a_5-6', 'name': 'name_a_5-6', 'ref': 'ref_a_5-6'},
		{'prefix': 'Double', 'url': 'a_5-7', 'name': 'name_a_5-7', 'ref': 'ref_a_5-7'},
		{'prefix': 'Double', 'url': 'a_5-8', 'name': 'name_a_5-8', 'ref': 'ref_a_5-8'},
		{'prefix': 'Double', 'url': 'a_5-9', 'name': 'name_a_5-9', 'ref': 'ref_a_5-9'},
		{'prefix': 'Double', 'url': 'a_5-10', 'name': 'name_a_5-10', 'ref': 'ref_a_5-10'},
		{'prefix': 'Double', 'url': 'a_5-11', 'name': 'name_a_5-11', 'ref': 'ref_a_5-11'},
	]

	Simple = []
	Circulaire = []
	Double = []

	for x in articles:
		if(x['prefix'] == 'Simple'):
			Simple.append(x)
		elif(x['prefix'] == 'Circulaire'):
			Circulaire.append(x)
		elif(x['prefix'] == 'Double'):
			Double.append(x)

	paginator_Simple = Paginator(Simple, 100)
	paginator_Circulaire = Paginator(Circulaire, 100)
	paginator_Double = Paginator(Double, 100)

	page = request.GET.get('page')
	try:
		Simple_list = paginator_Simple.page(page)
		Circulaire_list = paginator_Circulaire.page(page)
		Double_list = paginator_Double.page(page)
	except PageNotAnInteger:
		Simple_list = paginator_Simple.page(1)
		Circulaire_list = paginator_Circulaire.page(1)
		Double_list = paginator_Double.page(1)
	except EmptyPage:
		Simple_list = paginator_Simple.page(paginator_Simple.num_pages)
		Circulaire_list = paginator_Circulaire.page(paginator_Circulaire.num_pages)
		Double_list = paginator_Double.page(paginator_Double.num_pages)
	context = {
		'name': 'index_eviers',
		'Simple_list': Simple_list,
		'Circulaire_list': Circulaire_list,
		'Double_list': Double_list,
	}
	return render(request, 'carre_app/index_eviers.html', context)

def index_robinetterie(request):
	articles = [
		{'prefix': 'Mitigeur', 'url': 'a_6-1', 'name': 'name_a_6-1', 'ref': 'ref_a_6-1'},
		{'prefix': 'Robinet', 'url': 'a_6-2', 'name': 'name_a_6-2', 'ref': 'ref_a_6-2'},
		{'prefix': 'Poussoir', 'url': 'a_6-3', 'name': 'name_a_6-3', 'ref': 'ref_a_6-3'},
		{'prefix': 'Siphon', 'url': 'a_6-4', 'name': 'name_a_6-4', 'ref': 'ref_a_6-4'},
		{'prefix': 'Colonne', 'url': 'a_6-5', 'name': 'name_a_6-5', 'ref': 'ref_a_6-5'},
		{'prefix': 'Pomme', 'url': 'a_6-6', 'name': 'name_a_6-6', 'ref': 'ref_a_6-6'},
		{'prefix': 'Mitigeur', 'url': 'a_6-7', 'name': 'name_a_6-7', 'ref': 'ref_a_6-7'},
		{'prefix': 'Robinet', 'url': 'a_6-8', 'name': 'name_a_6-8', 'ref': 'ref_a_6-8'},
		{'prefix': 'Poussoir', 'url': 'a_6-9', 'name': 'name_a_6-9', 'ref': 'ref_a_6-9'},
		{'prefix': 'Siphon', 'url': 'a_6-10', 'name': 'name_a_6-10', 'ref': 'ref_a_6-10'},
		{'prefix': 'Colonne', 'url': 'a_6-11', 'name': 'name_a_6-11', 'ref': 'ref_a_6-11'},
		{'prefix': 'Pomme', 'url': 'a_6-12', 'name': 'name_a_6-12', 'ref': 'ref_a_6-12'},
		{'prefix': 'Mitigeur', 'url': 'a_6-13', 'name': 'name_a_6-13', 'ref': 'ref_a_6-13'},
		{'prefix': 'Robinet', 'url': 'a_6-14', 'name': 'name_a_6-14', 'ref': 'ref_a_6-14'},
		{'prefix': 'Poussoir', 'url': 'a_6-15', 'name': 'name_a_6-15', 'ref': 'ref_a_6-15'},
		{'prefix': 'Siphon', 'url': 'a_6-16', 'name': 'name_a_6-16', 'ref': 'ref_a_6-16'},
		{'prefix': 'Colonne', 'url': 'a_6-17', 'name': 'name_a_6-17', 'ref': 'ref_a_6-17'},
	]

	Mitigeur = []
	Robinet = []
	Poussoir = []
	Siphon = []
	Colonne = []
	Pomme = []

	for x in articles:
		if(x['prefix'] == 'Mitigeur'):
			Mitigeur.append(x)
		elif(x['prefix'] == 'Robinet'):
			Robinet.append(x)
		elif(x['prefix'] == 'Poussoir'):
			Poussoir.append(x)
		elif(x['prefix'] == 'Siphon'):
			Siphon.append(x)
		elif(x['prefix'] == 'Colonne'):
			Colonne.append(x)
		elif(x['prefix'] == 'Pomme'):
			Pomme.append(x)

	paginator_Mitigeur = Paginator(Mitigeur, 100)
	paginator_Robinet = Paginator(Robinet, 100)
	paginator_Poussoir = Paginator(Poussoir, 100)
	paginator_Siphon = Paginator(Siphon, 100)
	paginator_Colonne = Paginator(Colonne, 100)
	paginator_Pomme = Paginator(Pomme, 100)

	page = request.GET.get('page')
	try:
		Mitigeur_list = paginator_Mitigeur.page(page)
		Robinet_list = paginator_Robinet.page(page)
		Poussoir_list = paginator_Poussoir.page(page)
		Siphon_list = paginator_Siphon.page(page)
		Colonne_list = paginator_Colonne.page(page)
		Pomme_list = paginator_Pomme.page(page)
	except PageNotAnInteger:
		Mitigeur_list = paginator_Mitigeur.page(1)
		Robinet_list = paginator_Robinet.page(1)
		Poussoir_list = paginator_Poussoir.page(1)
		Siphon_list = paginator_Siphon.page(1)
		Colonne_list = paginator_Colonne.page(1)
		Pomme_list = paginator_Pomme.page(1)
	except EmptyPage:
		Mitigeur_list = paginator_Mitigeur.page(paginator_Mitigeur.num_pages)
		Robinet_list = paginator_Robinet.page(paginator_Robinet.num_pages)
		Poussoir_list = paginator_Poussoir.page(paginator_Poussoir.num_pages)
		Siphon_list = paginator_Siphon.page(paginator_Siphon.num_pages)
		Colonne_list = paginator_Colonne.page(paginator_Colonne.num_pages)
		Pomme_list = paginator_Pomme.page(paginator_Pomme.num_pages)
	context = {
		'name': 'index_robinetterie',
		'Mitigeur_list': Mitigeur_list,
		'Robinet_list': Robinet_list,
		'Poussoir_list': Poussoir_list,
		'Siphon_list': Siphon_list,
		'Colonne_list': Colonne_list,
		'Pomme_list': Pomme_list,
	}
	return render(request, 'carre_app/index_robinetterie.html', context)

def index_accessoires(request):
	articles = [
		{'prefix': 'Titanic', 'url': 'a_7-1', 'name': 'name_a_7-1', 'ref': 'ref_a_7-1'},
		{'prefix': 'Titanic', 'url': 'a_7-2', 'name': 'name_a_7-2', 'ref': 'ref_a_7-2'},
		{'prefix': 'Titanic', 'url': 'a_7-3', 'name': 'name_a_7-3', 'ref': 'ref_a_7-3'},
		{'prefix': 'Titanic', 'url': 'a_7-4', 'name': 'name_a_7-4', 'ref': 'ref_a_7-4'},
		{'prefix': 'Titanic', 'url': 'a_7-5', 'name': 'name_a_7-5', 'ref': 'ref_a_7-5'},
		{'prefix': 'Titanic', 'url': 'a_7-6', 'name': 'name_a_7-6', 'ref': 'ref_a_7-6'},
		{'prefix': 'Titanic', 'url': 'a_7-7', 'name': 'name_a_7-7', 'ref': 'ref_a_7-7'},
		{'prefix': 'Titanic', 'url': 'a_7-8', 'name': 'name_a_7-8', 'ref': 'ref_a_7-8'},
		{'prefix': 'Titanic', 'url': 'a_7-9', 'name': 'name_a_7-9', 'ref': 'ref_a_7-9'},
		{'prefix': 'Titanic', 'url': 'a_7-10', 'name': 'name_a_7-10', 'ref': 'ref_a_7-10'},
		{'prefix': 'Flora', 'url': 'a_7-11', 'name': 'name_a_7-11', 'ref': 'ref_a_7-11'},
		{'prefix': 'Flora', 'url': 'a_7-12', 'name': 'name_a_7-12', 'ref': 'ref_a_7-12'},
		{'prefix': 'Flora', 'url': 'a_7-13', 'name': 'name_a_7-13', 'ref': 'ref_a_7-13'},
		{'prefix': 'Flora', 'url': 'a_7-14', 'name': 'name_a_7-14', 'ref': 'ref_a_7-14'},
		{'prefix': 'Flora', 'url': 'a_7-15', 'name': 'name_a_7-15', 'ref': 'ref_a_7-15'},
		{'prefix': 'Flora', 'url': 'a_7-16', 'name': 'name_a_7-16', 'ref': 'ref_a_7-16'},
		{'prefix': 'Flora', 'url': 'a_7-17', 'name': 'name_a_7-17', 'ref': 'ref_a_7-17'},
		{'prefix': 'Flora', 'url': 'a_7-18', 'name': 'name_a_7-18', 'ref': 'ref_a_7-18'},
		{'prefix': 'Flora', 'url': 'a_7-19', 'name': 'name_a_7-19', 'ref': 'ref_a_7-19'},
		{'prefix': 'Flora', 'url': 'a_7-20', 'name': 'name_a_7-20', 'ref': 'ref_a_7-20'},
		{'prefix': 'DE LUXE', 'url': 'a_7-21', 'name': 'name_a_7-21', 'ref': 'ref_a_7-21'},
		{'prefix': 'DE LUXE', 'url': 'a_7-22', 'name': 'name_a_7-22', 'ref': 'ref_a_7-22'},
		{'prefix': 'DE LUXE', 'url': 'a_7-23', 'name': 'name_a_7-23', 'ref': 'ref_a_7-23'},
		{'prefix': 'DE LUXE', 'url': 'a_7-24', 'name': 'name_a_7-24', 'ref': 'ref_a_7-24'},
		{'prefix': 'DE LUXE', 'url': 'a_7-25', 'name': 'name_a_7-25', 'ref': 'ref_a_7-25'},
		{'prefix': 'DE LUXE', 'url': 'a_7-26', 'name': 'name_a_7-26', 'ref': 'ref_a_7-26'},
		{'prefix': 'DE LUXE', 'url': 'a_7-27', 'name': 'name_a_7-27', 'ref': 'ref_a_7-27'},
		{'prefix': 'DE LUXE', 'url': 'a_7-28', 'name': 'name_a_7-28', 'ref': 'ref_a_7-28'},
		{'prefix': 'DE LUXE', 'url': 'a_7-29', 'name': 'name_a_7-29', 'ref': 'ref_a_7-29'},
		{'prefix': 'DE LUXE', 'url': 'a_7-30', 'name': 'name_a_7-30', 'ref': 'ref_a_7-30'},
		{'prefix': 'ELEGANCE', 'url': 'a_7-31', 'name': 'name_a_7-31', 'ref': 'ref_a_7-31'},
		{'prefix': 'ELEGANCE', 'url': 'a_7-32', 'name': 'name_a_7-32', 'ref': 'ref_a_7-32'},
		{'prefix': 'ELEGANCE', 'url': 'a_7-33', 'name': 'name_a_7-33', 'ref': 'ref_a_7-33'},
		{'prefix': 'ELEGANCE', 'url': 'a_7-34', 'name': 'name_a_7-34', 'ref': 'ref_a_7-34'},
		{'prefix': 'ELEGANCE', 'url': 'a_7-35', 'name': 'name_a_7-35', 'ref': 'ref_a_7-35'},
		{'prefix': 'ELEGANCE', 'url': 'a_7-36', 'name': 'name_a_7-36', 'ref': 'ref_a_7-36'},
		{'prefix': 'ELEGANCE', 'url': 'a_7-37', 'name': 'name_a_7-37', 'ref': 'ref_a_7-37'},
		{'prefix': 'ELEGANCE', 'url': 'a_7-38', 'name': 'name_a_7-38', 'ref': 'ref_a_7-38'},
		{'prefix': 'ELEGANCE', 'url': 'a_7-39', 'name': 'name_a_7-39', 'ref': 'ref_a_7-39'},
		{'prefix': 'ELEGANCE', 'url': 'a_7-40', 'name': 'name_a_7-40', 'ref': 'ref_a_7-40'},
		{'prefix': 'KUMRU', 'url': 'a_7-41', 'name': 'name_a_7-41', 'ref': 'ref_a_7-41'},
		{'prefix': 'KUMRU', 'url': 'a_7-42', 'name': 'name_a_7-42', 'ref': 'ref_a_7-42'},
		{'prefix': 'KUMRU', 'url': 'a_7-43', 'name': 'name_a_7-43', 'ref': 'ref_a_7-43'},
		{'prefix': 'KUMRU', 'url': 'a_7-44', 'name': 'name_a_7-44', 'ref': 'ref_a_7-44'},
		{'prefix': 'KUMRU', 'url': 'a_7-45', 'name': 'name_a_7-45', 'ref': 'ref_a_7-45'},
		{'prefix': 'KUMRU', 'url': 'a_7-46', 'name': 'name_a_7-46', 'ref': 'ref_a_7-46'},
		{'prefix': 'KUMRU', 'url': 'a_7-47', 'name': 'name_a_7-47', 'ref': 'ref_a_7-47'},
		{'prefix': 'KUMRU', 'url': 'a_7-48', 'name': 'name_a_7-48', 'ref': 'ref_a_7-48'},
		{'prefix': 'KUMRU', 'url': 'a_7-49', 'name': 'name_a_7-49', 'ref': 'ref_a_7-49'},
		{'prefix': 'KUMRU', 'url': 'a_7-50', 'name': 'name_a_7-50', 'ref': 'ref_a_7-50'},
		{'prefix': 'TEGRA', 'url': 'a_7-51', 'name': 'name_a_7-51', 'ref': 'ref_a_7-51'},
		{'prefix': 'TEGRA', 'url': 'a_7-52', 'name': 'name_a_7-52', 'ref': 'ref_a_7-52'},
		{'prefix': 'TEGRA', 'url': 'a_7-53', 'name': 'name_a_7-53', 'ref': 'ref_a_7-53'},
		{'prefix': 'TEGRA', 'url': 'a_7-54', 'name': 'name_a_7-54', 'ref': 'ref_a_7-54'},
		{'prefix': 'TEGRA', 'url': 'a_7-55', 'name': 'name_a_7-55', 'ref': 'ref_a_7-55'},
		{'prefix': 'TEGRA', 'url': 'a_7-56', 'name': 'name_a_7-56', 'ref': 'ref_a_7-56'},
		{'prefix': 'TEGRA', 'url': 'a_7-57', 'name': 'name_a_7-57', 'ref': 'ref_a_7-57'},
		{'prefix': 'TEGRA', 'url': 'a_7-58', 'name': 'name_a_7-58', 'ref': 'ref_a_7-58'},
		{'prefix': 'TEGRA', 'url': 'a_7-59', 'name': 'name_a_7-59', 'ref': 'ref_a_7-59'},
		{'prefix': 'TEGRA', 'url': 'a_7-60', 'name': 'name_a_7-60', 'ref': 'ref_a_7-60'},
		{'prefix': 'Autre', 'url': 'a_7-61', 'name': 'name_a_7-61', 'ref': 'ref_a_7-61'},
		{'prefix': 'Autre', 'url': 'a_7-62', 'name': 'name_a_7-62', 'ref': 'ref_a_7-62'},
		{'prefix': 'Autre', 'url': 'a_7-63', 'name': 'name_a_7-63', 'ref': 'ref_a_7-63'},
		{'prefix': 'Autre', 'url': 'a_7-64', 'name': 'name_a_7-64', 'ref': 'ref_a_7-64'},
		{'prefix': 'Autre', 'url': 'a_7-65', 'name': 'name_a_7-65', 'ref': 'ref_a_7-65'},
		{'prefix': 'Autre', 'url': 'a_7-66', 'name': 'name_a_7-66', 'ref': 'ref_a_7-66'},
		{'prefix': 'Autre', 'url': 'a_7-67', 'name': 'name_a_7-67', 'ref': 'ref_a_7-67'},
		{'prefix': 'Autre', 'url': 'a_7-68', 'name': 'name_a_7-68', 'ref': 'ref_a_7-68'},
		{'prefix': 'Autre', 'url': 'a_7-69', 'name': 'name_a_7-69', 'ref': 'ref_a_7-69'},
		{'prefix': 'Autre', 'url': 'a_7-70', 'name': 'name_a_7-70', 'ref': 'ref_a_7-70'},
		{'prefix': 'Autre', 'url': 'a_7-71', 'name': 'name_a_7-71', 'ref': 'ref_a_7-71'},
		{'prefix': 'Autre', 'url': 'a_7-72', 'name': 'name_a_7-72', 'ref': 'ref_a_7-72'},
		{'prefix': 'Autre', 'url': 'a_7-73', 'name': 'name_a_7-73', 'ref': 'ref_a_7-73'},
		{'prefix': 'Autre', 'url': 'a_7-74', 'name': 'name_a_7-74', 'ref': 'ref_a_7-74'},
		{'prefix': 'Autre', 'url': 'a_7-75', 'name': 'name_a_7-75', 'ref': 'ref_a_7-75'},
		{'prefix': 'Autre', 'url': 'a_7-76', 'name': 'name_a_7-76', 'ref': 'ref_a_7-76'},
		{'prefix': 'Autre', 'url': 'a_7-77', 'name': 'name_a_7-77', 'ref': 'ref_a_7-77'},
		{'prefix': 'Autre', 'url': 'a_7-78', 'name': 'name_a_7-78', 'ref': 'ref_a_7-78'},
		{'prefix': 'Autre', 'url': 'a_7-79', 'name': 'name_a_7-79', 'ref': 'ref_a_7-79'},
		{'prefix': 'Autre', 'url': 'a_7-80', 'name': 'name_a_7-80', 'ref': 'ref_a_7-80'},
	]

	Titanic = []
	Flora = []
	DE_LUXE = []
	ELEGANCE = []
	KUMRU = []
	TEGRA = []
	Autre = []

	for x in articles:
		if(x['prefix'] == 'Titanic'):
			Titanic.append(x)
		elif(x['prefix'] == 'Flora'):
			Flora.append(x)
		elif(x['prefix'] == 'DE LUXE'):
			DE_LUXE.append(x)
		elif(x['prefix'] == 'ELEGANCE'):
			ELEGANCE.append(x)
		elif(x['prefix'] == 'KUMRU'):
			KUMRU.append(x)
		elif(x['prefix'] == 'TEGRA'):
			TEGRA.append(x)
		elif(x['prefix'] == 'Autre'):
			Autre.append(x)

	paginator_Titanic = Paginator(Titanic, 100)
	paginator_Flora = Paginator(Flora, 100)
	paginator_DE_LUXE = Paginator(DE_LUXE, 100)
	paginator_ELEGANCE = Paginator(ELEGANCE, 100)
	paginator_KUMRU = Paginator(KUMRU, 100)
	paginator_TEGRA = Paginator(TEGRA, 100)
	paginator_Autre = Paginator(Autre, 100)

	page = request.GET.get('page')
	try:
		Titanic_list = paginator_Titanic.page(page)
		Flora_list = paginator_Flora.page(page)
		DE_LUXE_list = paginator_DE_LUXE.page(page)
		ELEGANCE_list = paginator_ELEGANCE.page(page)
		KUMRU_list = paginator_KUMRU.page(page)
		TEGRA_list = paginator_TEGRA.page(page)
		Autre_list = paginator_Autre.page(page)
	except PageNotAnInteger:
		Titanic_list = paginator_Titanic.page(1)
		Flora_list = paginator_Flora.page(1)
		DE_LUXE_list = paginator_DE_LUXE.page(1)
		ELEGANCE_list = paginator_ELEGANCE.page(1)
		KUMRU_list = paginator_KUMRU.page(1)
		TEGRA_list = paginator_TEGRA.page(1)
		Autre_list = paginator_Autre.page(1)
	except EmptyPage:
		Titanic_list = paginator_Titanic.page(paginator_Titanic.num_pages)
		Flora_list = paginator_Flora.page(paginator_Flora.num_pages)
		DE_LUXE_list = paginator_DE_LUXE.page(paginator_DE_LUXE.num_pages)
		ELEGANCE_list = paginator_ELEGANCE.page(paginator_ELEGANCE.num_pages)
		KUMRU_list = paginator_KUMRU.page(paginator_KUMRU.num_pages)
		TEGRA_list = paginator_TEGRA.page(paginator_TEGRA.num_pages)
		Autre_list = paginator_Autre.page(paginator_Autre.num_pages)
	context = {
		'name': 'index_accessoires',
		'Titanic_list': Titanic_list,
		'Flora_list': Flora_list,
		'DE_LUXE_list': DE_LUXE_list,
		'ELEGANCE_list': ELEGANCE_list,
		'KUMRU_list': KUMRU_list,
		'TEGRA_list': TEGRA_list,
		'Autre_list': Autre_list,
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