from django.contrib import admin
from django.urls import path

from produtos.views import ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView, ProdutoCompleteView, ProdutoDetailView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", ProdutoListView.as_view(), name="produto_list"),
    path("create", ProdutoCreateView.as_view(),  name="produto_create"),
    path("update/<int:pk>", ProdutoUpdateView.as_view(),  name="produto_update"),
    path("delete/<int:pk>", ProdutoDeleteView.as_view(),  name="produto_delete"),
    path("complete/<int:pk>", ProdutoCompleteView.as_view(),  name="produto_complete"),
    path("detail/<int:pk>", ProdutoDetailView.as_view(),  name="produto_detail"),
]
