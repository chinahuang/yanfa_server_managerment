# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import asset
from guardian.admin import GuardedModelAdmin

class AssetAdmin(GuardedModelAdmin):
    search_fields = ('inner_ip','asset_ID',)
    list_display = ('asset_ID','inner_ip','manage_ip','server_model','server_system','server_place','server_cabinet')
    list_display_links = ('asset_ID','inner_ip',)


admin.site.register(asset,AssetAdmin)