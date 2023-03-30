#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
账户相关：注册、登录、注销、短信
"""
from django.shortcuts import render, HttpResponse
from web.forms.account import RegisterModelForm


def register(request):
    form = RegisterModelForm()
    return render(request, 'register.html', {'form': form})
