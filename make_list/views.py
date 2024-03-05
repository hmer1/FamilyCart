from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from accounts.forms import CustomCreateUserForm
from accounts.models import CustomUser

from django.contrib import messages
from django.shortcuts import render, redirect
from django.db import IntegrityError


def make_list(request):
    return HttpResponsw("ja to pisze")