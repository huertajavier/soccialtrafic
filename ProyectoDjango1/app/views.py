"""
Definition of views.
"""

from django.shortcuts import render

from django.views.generic import FormView,CreateView,TemplateView
from django.core.urlresolvers import reverse_lazy
from .models import *
from .forms import *
from django.core import serializers
from django.http import HttpResponse


class Signup(FormView):
	template_name = 'app/signup.html'
	form_class = Usuario_Form
	success_url = reverse_lazy('login')

	def form_valid(self, form):

		user = form.save()
		p = Usuario_m()
		p.Nombre = user
		p.Telefono = form.cleaned_data['Telefono']
		p.Correo = form.cleaned_data['Correo']
		p.Direccion = form.cleaned_data['Direccion']
		p.Avatar=form.cleaned_data['Avatar']

		p.save()

		return super(Signup, self).form_valid(form)

def home(request):
    return render(request,'app/index.html')

def contact(request):
    return render(request,'app/contact.html')

def about(request):
    return render(request,'app/about.html')


def wsDenuncia(request):
	data = serializers.serialize('json', Denuncia2.objects.all(user='superadmin'))
	 #En lugar de json se puede poner xml
	#data = serializers.serialize('json', Denuncia.objects.raw("select d.titulo,d.descripcion,d.latitud,d.longitud,d.id from app_denuncia d where d.img is not null and dvideo is not null")) 
	return HttpResponse(data, content_type='application/json')



class Denuncia_sdfgdf(CreateView):
	models = Denuncia_m
	form_class = Denuncia_Form
	template_name = 'app/denuncia.html'
	success_url = reverse_lazy('login')

def Denuncia(request):
    form=Denuncia_Form(request.POST or None,request.FILES or None)
    if request.method=="POST":
        if form.is_valid():
            instance=form.save(commit=False)
            titulo = form.cleaned_data.get('titulo')
            descripcion = form.cleaned_data.get('descripcion')
            latitud = form.cleaned_data.get("latitud")
            longitud = form.cleaned_data.get("longitud")
            img = form.cleaned_data.get("img")
            video = form.cleaned_data.get("video")
            form.save()
    return render(request, 'app/denuncia.html',{'form':form})
	
def Denuncia_dsfdsf(request):
	form=Denuncia_Form(request.POST or None)
	p=Denuncia_m()
	if request.method=="POST":
		if form.is_valid():
			user=form.cleaned_data['user']
			titulo = form.cleaned_data['titulo']
			descripcion = form.cleaned_data['descripcion']
			latitud = form.cleaned_data["latitud"]
			longitud = form.cleaned_data["longitud"]
			img = form.cleaned_data["img"]
			video = form.cleaned_data["video"]


			p.img = img
			p.video = video
			p.user=user
			#p.user=user
			p.titulo=titulo
			p.longitud=longitud
			p.latitud=latitud
			p.descripcion = descripcion

			p.save()
			form=Ubicar_Form()

	return render(request,'app/denuncia.html',{"form":form})

class Facebook_view(TemplateView):
	template_name='app/facebook.html'