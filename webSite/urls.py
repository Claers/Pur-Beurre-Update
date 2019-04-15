""" Urls for the webSite app """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="acceuil"),
    path('success', views.index, name="acceuil_login"),
    path('search', views.search, name="recherche"),
    path('connexion', views.connexion, name="connexion"),
    path('deconnexion', views.logout_user, name="logout"),
    path('product/<product_name>', views.product_info, name="produit"),
    path('product/<product_name>/<substitute_name>',
         views.product_substitute_info, name="produit_substitut"),
    path('favoris/<product_name>/<substitute_name>',
         views.register_fav, name="favoris_register"),
    path('remove/<product_name>/<substitute_name>',
         views.remove_fav, name="favoris_remove"),
    path('admin/fill', views.fill_view, name="fill"),
    path('admin/ajax/fill', views.fill_data, name="fill_data"),
    path('admin/fill_success', views.fill_success, name="fill_success"),
    path('user', views.user, name="user"),
    path('favoris', views.favorites, name="favoris"),
    path('admin/delete', views.del_data, name="deleteDB"),
    path('legal', views.legal_mentions, name="legal")
]
