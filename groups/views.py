from django.shortcuts import render
from django.contrib import messages
from django.db import IntegrityError
from . import models

# Create your views here.
from django.contrib.auth.mixins import (LoginRequiredMixin, 
                                            PermissionRequiredMixin)
from django.urls import reverse
from django.views import generic
from groups.models import Group
from django.shortcuts import get_object_or_404

class CreateGroup(LoginRequiredMixin,generic.CreateView):
    fields = ('location', 'description', 'date')
    model = Group


class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group


