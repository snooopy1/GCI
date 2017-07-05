from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_renta(request):
	return render(request, 'renta/index.html')