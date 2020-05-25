from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
	matchs = Match.objects.all()
	classements = Classement.objects.filter(competition__competition_name="la liga")
	context = {'matchs' : matchs,
				'classements' : classements}
	return render(request, 'presentation/index.html', context)
	
