from django.shortcuts import render

from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _


def testlang(request):
    return HttpResponse(_('Welcome to language translation!'))
