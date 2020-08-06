from django.shortcuts import render
from django.views.generic import ListView
from core.models import Product

# Create your views here.
class SearchProductView(ListView):
    template_name = 'products/list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        result = request.GET.get
        query = request.GET.get('q', None)
        if query is not None:
            return Product.objects.filter(title__contains= query)
        return Product.objects.featured()
