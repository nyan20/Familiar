from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from myapp.familia.forms import FamiliaForm
from myapp.familia.models import Familia

# Create your views here.

def index(request):
	return render(request, 'familia/index.html')

def familia_view(request):
	if request.method == 'POST':
		form = FamiliaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('familia:familia_listar')
	else:
		form = FamiliaForm()
	return render(request, 'familia/familia_form.html', {'form':form})

def familia_list(request):
	familia = Familia.objects.all().order_by('id')
	contexto = {'familias': familia}
	return render(request, 'familia/familia_list.html', contexto)

def familia_edit(request, id_familia):
	familia = Familia.objects.get(id=id_familia)
	if request.method == 'GET':
		form = FamiliaForm(instance=familia)
	else:
		form = FamiliaForm(request.POST, instance=familia)
		if form.is_valid():
			form.save()
		return redirect('familia:familia_listar')	
	return render(request, 'familia/familia_form.html', {'form':form})

def familia_delete(request, id_familia):
	familia = Familia.objects.get(id=id_familia)
	if request.method == 'POST':
		familia.delete()
		return redirect('familia:familia_listar')
	return render(request, 'familia/familia_delete.html', {'familia':familia})

class FamiliaList(ListView):
	model = Familia
	template_name = 'familia/familia_list.html'

class FamiliaCreate(CreateView):
	model = Familia
	form_class = FamiliaForm
	template_name = 'familia/familia_form.html'
	success_url = reverse_lazy('familia:familia_listar')

class FamiliaUpdate(UpdateView):
	model = Familia
	form_class = FamiliaForm
	template_name = 'familia/familia_form.html'
	success_url = reverse_lazy('familia:familia_listar')

class FamiliaDelete(DeleteView):
	model = Familia
	template_name = 'familia/familia_delete.html'
	success_url = reverse_lazy('familia:familia_listar')

