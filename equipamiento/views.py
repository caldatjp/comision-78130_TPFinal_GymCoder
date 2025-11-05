from equipamiento.forms import EquipamientoForm
from equipamiento.models import Equipamiento
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

class EquipamientoListView(ListView):
    model = Equipamiento
    template_name = 'equipamiento/equipamiento_list.html'
    context_object_name = "equipamientos"
    
    def get_queryset(self):
        query = self.request.GET.get("q", '')
        if query:
            return Equipamiento.objects.filter(nombre_ref__icontains=query).order_by("-fecha_alta")
        return Equipamiento.objects.all()

class EquipamientoCreateView(CreateView):
    model = Equipamiento
    form_class = EquipamientoForm
    template_name = "equipamiento/equipamiento_form.html"
    success_url = reverse_lazy('equipamiento_list')

class EquipamientoUpdateView(UpdateView):
    model = Equipamiento
    form_class = EquipamientoForm
    template_name = "equipamiento/equipamiento_form.html"
    success_url = reverse_lazy('equipamiento_list')
    slug_field = 'codigo'
    slug_url_kwarg = 'codigo'

class EquipamientoDeleteView(DeleteView):
    model = Equipamiento
    template_name = "equipamiento/equipamiento_confirm_delete.html"
    success_url = reverse_lazy('equipamiento_list')
    slug_field = 'codigo'
    slug_url_kwarg = 'codigo'

class EquipamientoDetailView(DetailView):
    model = Equipamiento
    template_name = "equipamiento/equipamiento_detail.html"
    context_object_name = "equipamiento"
    slug_field = "codigo"
    slug_url_kwarg = "codigo"
