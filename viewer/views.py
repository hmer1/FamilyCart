from django.http import HttpResponse
from django.shortcuts import render
from viewer.models import Product
# from django.views import View
# from django.views.generic import TemplateView
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from viewer.forms import ProductForm
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


def products(request):
    return render(
        request, template_name='products.html',
        context={'products': Product.objects.all()}
  )


class ProductsView(View):
    def get(self, request):
        return render(
            request, template_name='products.html',
            context={'products': Product.objects.all()}
        )


class ProductsView(TemplateView):
    template_name = 'products.html'
    extra_context = {'products': Product.objects.all()}
'''


def hello(request, s0):
    s1 = request.GET.get('s1', '')
    return render(
        request, template_name='hello.html',
        context={'adjectives': [s0, s1, 'beautiful', 'wonderful']}
    )


class ProductsView(ListView):
    template_name = 'products.html'
    model = Product


class ProductCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = ProductForm
    success_url = reverse_lazy('index')
    permission_required = 'viewer.add_product'

    def form_invalid(self, form):
        LOGGER.warning(">>>>>>User provided invalid data.")
        return super().form_invalid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('index')
    permission_required = 'viewer.change_product'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data while updating a product.')
        return super().form_invalid(form)


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'product_confirm_delete.html'
    model = Product
    success_url = reverse_lazy('index')
    permission_required = 'viewer.delete_product'






