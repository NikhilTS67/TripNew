from django.shortcuts import render
from. models import album
from .models import Team

# Create your views here.


def fstfn(requests):
    obj = album.objects.all()
    obj2 = Team.objects.all()
    return render(requests, 'index.html', {'result': obj, 'team': obj2})



# def sndfn(requests):
#     return render(requests,'snd.html')
#
# def thdfn(requests):
#    return HttpResponse('Third Response')
#
# def forfn(requests):
#     return render(requests, 'frt.html')