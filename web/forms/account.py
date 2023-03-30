#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django import forms
from app01 import models
from django.core.validators import RegexValidator


class RegisterModelForm(forms.ModelForm):
    mobile_phone = forms.CharField(label='手机号', validators=[RegexValidator('^(1[3|4|5|6|7|8|9])\d+{9}$', '手机号格式错误')])
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='确认密码', widget=forms.PasswordInput())
    code = forms.CharField(label='验证码')
    class Meta:
        model = models.UserInfo
        # fields = "__all__"
        fields = ['username', 'email', 'mobile_phone', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class']='form-control'
            field.widget.attrs['placeholder']='请输入%s'%(field.label)
