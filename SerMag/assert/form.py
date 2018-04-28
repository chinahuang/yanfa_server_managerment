# -*- coding:utf-8 -*-

from django import forms
from .models import asset
from django.forms import ValidationError

class AssetForm(forms.ModelForm):
    class Meta:
        model = asset
        fields = '__all__'

        labels = {
            'asset_ID':'资产号',
            'inner_ip':'内网ip',
        }
        widgets = {

            'server_info':forms.Textarea(
                attrs= {'cols':80,'rows':3}
            ),
            'func':forms.Textarea(
                attrs={'cols':80,'row':3}
            ),
            'desc':forms.Textarea(
                attrs={'cols':80,'row':3}
            )

        }

        help_texts = {
            'asset_ID':'服务器资产号',
            'inner_ip':'服务器内网ip',
        }
        error_messages = {
            'asset_ID':{
                'max_length':('太短了'),
            }
        }