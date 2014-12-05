from django.http import HttpResponse
from django.views.generic.base import View

class Index(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Know Your Plans")
