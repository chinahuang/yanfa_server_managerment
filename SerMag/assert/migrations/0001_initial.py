# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-27 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(blank=True, max_length=48, null=True, verbose_name='\u4e3b\u673a\u540d')),
                ('asset_ID', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u8d44\u4ea7\u53f7')),
                ('server_model', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u578b\u53f7')),
                ('server_system', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u7cfb\u7edf')),
                ('server_ID', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u5e8f\u5217\u53f7')),
                ('inner_ip', models.GenericIPAddressField(unique=True, verbose_name='\u5185\u7f51IP')),
                ('manage_ip', models.GenericIPAddressField(unique=True, verbose_name='\u7ba1\u7406IP')),
                ('server_admin', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u7ba1\u7406\u7528\u6237')),
                ('server_admin_passwd', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u7ba1\u7406\u7528\u6237\u5bc6\u7801')),
                ('server_place', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u8d44\u4ea7\u5730\u70b9')),
                ('server_cabinet', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u673a\u67dc\u4fe1\u606f')),
                ('is_active', models.BooleanField(default=True, verbose_name='\u662f\u5426\u542f\u7528')),
                ('is_check', models.BooleanField(default=False, verbose_name='\u662f\u5426\u68c0\u67e5')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'db_table': 'asset',
                'verbose_name': '\u8d44\u4ea7\u7ba1\u7406',
                'verbose_name_plural': '\u8d44\u4ea7\u7ba1\u7406',
            },
        ),
    ]
