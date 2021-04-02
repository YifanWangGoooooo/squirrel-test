from django.shortcuts import render
from .models import Squirrel
from django.shortcuts import get_object_or_404
def index(request):
   squirrels= Squirrel.objects.all()
   context = {'squirrels':squirrels,}
   return render(request, 'sightings/index.html', context)

def detail(request,Unique_Squirrel_ID):
   squirrel=get_object_or_404( Squirrel, Unique_Squirrel_ID=Unique_Squirrel_ID)
   context = {
           'squirrel':squirrel,
   }
   return render(request, 'sightings/detail.html', context)
# Create your views here.    
