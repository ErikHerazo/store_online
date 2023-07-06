from django.shortcuts import render
from utils.mongo_utils import db
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@csrf_exempt
def index(request):
    return(request)