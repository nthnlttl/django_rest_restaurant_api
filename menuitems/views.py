from rest_framework import generics
from .models import Menuitems

# Create your views here.

class MenuitemListView(generics.ListAPIView):
    model = Menuitems
    template_name = 'menu_list.html'