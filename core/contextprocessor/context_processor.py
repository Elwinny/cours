
from core.models import *

def get_setting(request):
    context = {
        'setting' : Setting.objects.first()
    }
    return context


def x(request):
    context = {
        'x' : x.objects.first(),
    }
    return context      