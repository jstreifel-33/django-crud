from django.views.generic import DeleteView, DetailView, CreateView, UpdateView, ListView
from django.urls import reverse_lazy

from snacks.models import Snack


# Create your views here.


class SnackListView(ListView):
    template_name = 'snacks_list.html'
    model = Snack


class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack


class SnackCreateView(CreateView):
    template_name = 'snack_create.html'
    model = Snack
    fields = ['title', 'purchaser', 'description']


class SnackUpdateView(UpdateView):
    template_name = 'snack_update.html'
    model = Snack
    fields = ['title', 'description']


class SnackDeleteView(DeleteView):
    template_name = 'snack_delete.html'
    model = Snack
    success_url = reverse_lazy('snacks_list')

