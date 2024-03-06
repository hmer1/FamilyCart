"""familycart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from viewer.models import Category, Product
# from viewer.views import hello, products
from viewer.views import hello, ProductsView, ProductCreateView, ProductUpdateView, ProductDeleteView
from django.contrib.auth.views import LoginView

admin.site.register(Category)
admin.site.register(Product)

urlpatterns = [
    # path('accounts/login/', LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls, name='admin'),
    path('', include('accounts.urls')),
    # path('hello', hello)
    # path('hello/<s>', hello)
    path('hello/<s0>', hello),
    # path('', products, name='index')
    path('', ProductsView.as_view(), name='index'),
    path('product/create', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('make_list/', include('make_list.urls'))
]





