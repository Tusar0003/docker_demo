from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view


@api_view(['GET'])
def base(request):
    return HttpResponse('<h1>Docker Demo API<h1/>')
