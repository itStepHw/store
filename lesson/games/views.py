from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from .models import Game


def index(request):
    game = Game.objects.filter(Q(price__lte=100) | Q(rating__gte=4) & Q(title__contains='title'))
    print(game)
    return HttpResponse(game)