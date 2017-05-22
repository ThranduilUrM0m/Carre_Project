from django.conf.urls import *
from . import views

app_name = 'carre_app'
urlpatterns = [
	url('^$', views.index_home, name='index_home'),
	url('^index_marque/$', views.index_marque, name='index_marque'),
	url('^index_collection/key_cat=(?P<categorie_id>[0-9]+)key_sub=(?P<subcategorie_id>[0-9]+)key_col=(?P<collection_id>[0-9]+)/$', views.index_collection, name='index_collection'),
	url('^index_adressendtel/$', views.index_adressendtel, name='index_adressendtel'),
	url('^index_categorie/key_cat=(?P<categorie_id>[0-9]+)/$', views.index_categorie, name='index_categorie'),
	url('^index_collectionsalledebains/$', views.index_collectionsalledebains, name='index_collectionsalledebains'),
	url('^index_sanitaire/$', views.index_sanitaire, name='index_sanitaire'),
	url('^index_baignoiresetreceveurs/$', views.index_baignoiresetreceveurs, name='index_baignoiresetreceveurs'),
	url('^index_miroirs/$', views.index_miroirs, name='index_miroirs'),
	url('^index_meubles/$', views.index_meubles, name='index_meubles'),
	url('^index_eviers/$', views.index_eviers, name='index_eviers'),
	url('^index_robinetterie/$', views.index_robinetterie, name='index_robinetterie'),
	url('^index_accessoires/$', views.index_accessoires, name='index_accessoires'),
	url('^Catalogue/$', views.Catalogue, name='Catalogue'),
]