from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    # dest1 = Destination()
    # dest1.name = "dhanush"
    # dest1.id = 1
    # dest1.price = 300
    return render(request, 'index.html',{'dest1_name': 'dhanush'})