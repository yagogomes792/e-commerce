from django.urls import path
from core.views import ProductDetailSlugView, ProductListView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('<slug:slug>/', ProductDetailSlugView.as_view())
]
