# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class asset(models.Model):
    hostname = models.CharField(max_length=48,null=True,blank=True,verbose_name='主机名')
    asset_ID = models.CharField(max_length=20,null=True,blank=True,verbose_name='资产号')
    server_model = models.CharField(max_length=20,null=True,blank=True)
    inner_ip = models.GenericIPAddressField(verbose_name='内网IP',unique=True)
    manage_ip = models.GenericIPAddressField(verbose_name='管理IP',unique=True)
