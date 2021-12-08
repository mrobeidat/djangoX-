from django.contrib.auth import update_session_auth_hash
from django.db.models import fields
from django.forms import models
from django.shortcuts import render
from .models import Snack
from django.urls import reverse_lazy
from django.views.generic import (

    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)
# Create your views here.


class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack


class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack
    context_object_name = 'snack_detail'


class SnackCreateView(CreateView):
    template_name = 'snack_create.html'
    model = Snack
    fields = ['title', 'description', 'purchaser']
  

class SnackDeleteView(DeleteView):
    template_name = 'snack_delete.html'
    model = Snack
    success_url = reverse_lazy('snacks')

class SnackUpdateView(UpdateView):
    template_name = 'snack_update.html'
    model = Snack
    fields = ['title', 'description']