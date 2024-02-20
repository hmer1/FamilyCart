from django.http import HttpResponse
from django.shortcuts import render
from viewer.models import Movie
# from django.views import View
# from django.views.generic import TemplateView
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from viewer.forms import MovieForm
from logging import getLogger
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

LOGGER = getLogger()
'''
def hello(request):
    return HttpResponse('Hello, world!')


def hello(request, s):
    return HttpResponse(f'Hello, {s} world!')    


def hello(request):
    s = request.GET.get('s', '')
    return HttpResponse(f'Hello, {s} world!')


def movies(request):
    return render(
        request, template_name='movies.html',
        context={'movies': Movie.objects.all()}
  )


class MoviesView(View):
    def get(self, request):
        return render(
            request, template_name='movies.html',
            context={'movies': Movie.objects.all()}
        )


class MoviesView(TemplateView):
    template_name = 'movies.html'
    extra_context = {'movies': Movie.objects.all()}
'''


def hello(request, s0):
    s1 = request.GET.get('s1', '')
    return render(
        request, template_name='hello.html',
        context={'adjectives': [s0, s1, 'beautiful', 'wonderful']}
    )


class MoviesView(ListView):
    template_name = 'movies.html'
    model = Movie


class MovieCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = MovieForm
    success_url = reverse_lazy('index')
    permission_required = 'viewer.add_movie'

    def form_invalid(self, form):
        LOGGER.warning(">>>>>>User provided invalid data.")
        return super().form_invalid(form)


class MovieUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('index')
    permission_required = 'viewer.change_movie'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data while updating a movie.')
        return super().form_invalid(form)


class MovieDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'movie_confirm_delete.html'
    model = Movie
    success_url = reverse_lazy('index')
    permission_required = 'viewer.delete_movie'






