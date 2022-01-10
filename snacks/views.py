from django.views.generic import TemplateView, DeleteView, DetailView, CreateView, UpdateView

from snacks.models import Snack


# Create your views here.


class SnackListView(TemplateView):
    template_name = 'snacks_list.html'
    model = Snack


class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack


class SnackCreateView(CreateView):
    template_name = 'snack_create.html'
    model = Snack


class SnackUpdateView(UpdateView):
    template_name = 'snack_update.html'
    model = Snack


class SnackDeleteView(DeleteView):
    template_name = 'snack_delete.html'
    model = Snack

