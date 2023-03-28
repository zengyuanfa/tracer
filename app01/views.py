from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from django.conf import settings
import random
from utils.tencent.sms import send_sms_single


def send_sms(request):
    """ 发送短信
            ?tpl=login  -> 1708821
            ?tpl=register -> 1708820
        """
    tpl = request.GET.get('tpl')
    template_id = settings.TENCENT_SMS_TEMPLATE.get(tpl)
    if not template_id:
        return HttpResponse('模板不存在')

    code = random.randrange(1000, 9999)
    res = send_sms_single('15989352018', template_id, [code, ])
    if res['result'] == 0:
        return HttpResponse('成功')
    else:
        return HttpResponse(res['errmsg'])


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


def register(request):
    form = RegisterModelForm()
    return render(request, 'app01/register.html', {'form': form})
