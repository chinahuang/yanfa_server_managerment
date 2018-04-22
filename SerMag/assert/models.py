# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class asset(models.Model):
    hostname = models.CharField(max_length=48,null=True,blank=True,verbose_name='主机名')
    asset_ID = models.CharField(max_length=20,null=True,blank=True,verbose_name='资产号')
    server_model = models.CharField(max_length=20,null=True,blank=True,verbose_name='型号')
    server_system = models.CharField(max_length=20,null=True,blank=True,verbose_name='系统')
    server_ID = models.CharField(max_length=20,null=True,blank=True,verbose_name='序列号')
    inner_ip = models.GenericIPAddressField(verbose_name='内网IP',unique=True)
    manage_ip = models.GenericIPAddressField(verbose_name='管理IP',unique=True)
    server_admin = models.CharField(max_length=20,null=True,blank=True,verbose_name='管理用户')
    server_admin_passwd = models.CharField(max_length=20,null=True,blank=True,verbose_name='管理用户密码')
    server_place = models.CharField(max_length=20,null=True,blank=True,verbose_name='资产地点')
    server_cabinet = models.CharField(max_length=20,null=True,blank=True,verbose_name='机柜信息')
    is_active = models.BooleanField(default=True,verbose_name='是否启用')
    is_check = models.BooleanField(default=False,verbose_name='是否检查')
    create_time = models.DateTimeField(auto_now_add=True,null=True,blank=True,verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True,null=True,blank=True,verbose_name='更新时间')

    class Meta:
        db_table = 'asset'
        verbose_name = '资产管理'
        verbose_name_plural = '资产管理'

        def __str__(self):
            return self.asset_ID


