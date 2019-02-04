from django.shortcuts import render
from django.http import HttpResponse
from .models import Sections, Articles
from django.views.generic import ListView, DetailView, CreateView, UpdateView


class BaseArticleListView(ListView):
    model = Articles
    queryset = Articles.objects.filter(sections__title__iexact='alpha')

    def get_context_data(self, **kwargs):
        context = super(BaseArticleListView, self).get_context_data(**kwargs)
        context['bravo'] = Articles.objects.filter(sections__title__iexact='Bravo')
        context['charlie'] = Articles.objects.filter(sections__title__iexact='Charlie')
        return context



class HomeView(BaseArticleListView):
    template_view="public/articles_list.html"


class SectionView(ListView):
    model = Sections
    template_view="public/sections_list.html"
