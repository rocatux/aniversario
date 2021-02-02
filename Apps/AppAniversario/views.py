from django.shortcuts import render
from django.shortcuts import redirect

from django.views.generic import TemplateView


class IndexView(TemplateView):
	template_name='inicio.html'

class GraciasView(TemplateView):
	template_name='gracias.html'