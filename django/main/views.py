<<<<<<< HEAD
from django.views.generic.base import TemplateView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return context
=======
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from seasons.models import Team


class HomeView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        teams = Team.objects.all()
        return render(request, self.template_name, {'teams': teams})
>>>>>>> upstream/master


class APIHomeView(APIView):
    '''
<<<<<<< HEAD
    This is the beginning of the MNL API. There's nothing here yet.
    '''
    permission_classes = (IsAuthenticated,)
=======
    [Back to Site Homepage](/)

    '''
    # # API Endpoints
    # - [Teams](/api/teams/)
>>>>>>> upstream/master

    def get(self, request, format=None):
        return Response()
