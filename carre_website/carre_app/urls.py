from django.conf.urls import *
from . import views

app_name = 'carre_app'
urlpatterns = [
	url('^$', views.index_home, name='index_home'),
	url('^index_marque/$', views.index_marque, name='index_marque'),
	url('^index_catalogue/$', views.index_catalogue, name='index_catalogue'),
	url('^index_adressendtel/$', views.index_adressendtel, name='index_adressendtel'),
	url('^index_groupe/$', views.index_groupe, name='index_groupe'),
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