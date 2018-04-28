# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import asset
from django.contrib.auth.models import User,Group
from guardian.shortcuts import assign_perm,get_perms
from guardian.core import ObjectPermissionChecker
from guardian.decorators import permission_required_or_403
from guardian.shortcuts import get_objects_for_group,get_objects_for_user
from django.contrib.auth.models import Permission
from guardian.models import UserObjectPermission,GroupObjectPermission
from django.views.generic import TemplateView,ListView,View,CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy

# Create your views here.

class AssetAll(TemplateView):
    template_name = 'asset/asset.html'

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(AssetAll,self).dispatch(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = {
            'asset_list':get_objects_for_user(self.request.user,'asset.read_asset')
        }
        kwargs.update(context)
        return super(AssetAll,self).get_context_data(**kwargs)

    def get(self,request):
        user = User.objects.get(username=request.user)
        ret = asset.objects.all
        return render(request,'asset/asset/html',{'asset_list':ret})


class