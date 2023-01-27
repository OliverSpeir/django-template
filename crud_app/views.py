from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from .models import Item


class ItemListView(ListView):
    template_name = 'list.html'
    model = Item


class ItemDetailView(DetailView):
    template_name = 'detail.html'
    model = Item
    fields = "__all__"


class ItemCreateView(CreateView):
    template_name = 'create.html'
    model = Item
    fields = "__all__"
    success_url = reverse_lazy('list')


class ItemUpdateView(UpdateView):
    template_name = 'update.html'
    model = Item
    fields = "__all__"
    success_url = reverse_lazy('list')


class ItemDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Item
    success_url = reverse_lazy('list')