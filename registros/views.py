from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from registros.models import Incluido


def portada(request):
    return render(request, "registros/portada.html")


@login_required
def inicio(request):
    return render(request, "registros/inicio.html")


class IncView(LoginRequiredMixin, ListView):
    model = Incluido
    template_name = 'registros/incluido_show.html'
    context_object_name = 'datos'


class IncDetailView(LoginRequiredMixin, DetailView):
    model = Incluido


class IncCreateView(LoginRequiredMixin, CreateView):
    model = Incluido
    fields = '__all__'


class IncUpdateView(LoginRequiredMixin, UpdateView):
    model = Incluido
    fields = '__all__'


class IncDeleteView(LoginRequiredMixin, DeleteView):
    model = Incluido
    success_url = reverse_lazy('inc_shows')


class IncLogsView(LoginRequiredMixin, ListView):
    model = Incluido
    template_name = 'registros/incluido_history.html'

    def get_context_data(self, **kwargs):
        context = super(IncLogsView, self).get_context_data(**kwargs)
        qry = Incluido.history.filter(id=self.kwargs['pk'])
        delta = []
        for i in range(0, len(qry)-1):
            delta.append(qry[i].diff_against(qry[i+1]))
        context['history'] = qry
        context['history_delta'] = delta

        return context


class IncHistoricoView(LoginRequiredMixin, ListView):
    queryset = Incluido.history.all()
    template_name = 'registros/incluido_audit.html'
    context_object_name = 'queryset'


def instructivos(request):
    pass


def goodcl(request):
    return render(request, 'registros/goodcl.html')


def aboutus(request):
    return render(request, 'registros/aboutus.html')
