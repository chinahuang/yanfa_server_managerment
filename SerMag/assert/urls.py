from django.conf.urls import url
from django.contrib import admin
from .import views

urlpatterns = [
    url('asset.html',views.AssetAll.as_view(),name='asset_list'),
    url('asset_add.html',views.AssetAdd.as_view(),name='asset_add'),
    # url('asset_del.html',views.AssetDel.as_views(),name='asset_del'),
]

app_name ='asset'