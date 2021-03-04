from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from django.views.generic.base import View

class CallbackView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('OK')

