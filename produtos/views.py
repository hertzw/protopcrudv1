from datetime import date
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from .models import Produto


class ProdutoListView(ListView):
    model = Produto
    paginate_by = 10
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        paginator = Paginator(Produto.objects.all(), 
        self.paginate_by) 
        page = self.request.GET.get('page') 
        produtos = paginator.get_page(page) 
        context['produto_list'] = produtos 
        return context

class ProdutoCreateView(CreateView):
    model = Produto
    fields = ["title","line", "scale", "vendor", "description", "quantity_in_stock","buy_price","msrp"]
    success_url = reverse_lazy("produto_list")

class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = ["title","line", "scale", "vendor", "description", "quantity_in_stock","buy_price","msrp"]
    success_url = reverse_lazy("produto_list")

class ProdutoDeleteView(DeleteView):
    model = Produto
    fields = ["title", "description"]
    success_url = reverse_lazy("produto_list")


class ProdutoCompleteView(View):
    def get(self, request, pk):
        produto = get_object_or_404(Produto, pk=pk)
        produto.mark_has_complete()
        return redirect("produto_list")


class ProdutoDetailView(DetailView):
    model = Produto
    fields = ["title", "scale"]
    success_url = reverse_lazy("produto_list")


