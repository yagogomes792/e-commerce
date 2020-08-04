from django.urls import path
from core.views import ProductDetailSlugView, ProductListView

app_name = "products"

urlpatterns = [
    path('', ProductListView.as_view()),
    path('<slug:slug>/', ProductDetailSlugView.as_view(), name='detail')
]
