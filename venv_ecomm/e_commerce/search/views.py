from django.shortcuts import render
from django.views.generic import ListView
from core.models import Product

# Create your views here.
class SearchProductView(ListView):
    template_name = 'search/view.html'

    def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)
            query = self.request.GET.get('q')
            context['query'] = query
            return context


    def get_queryset(self, *args, **kwargs):
        request = self.request
        result = request.GET.get
        query = request.GET.get('q', None)
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.featured()
