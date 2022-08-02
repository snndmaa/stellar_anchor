import json
from django.http import HttpResponse
from django.views.generic import View

from braces.views import CsrfExcemptMixin


class ProcessHookView(CsrfExcemptMixin, View):
    def post(self, request, *args, **kwargs):
        print(json.loads(request.body))
        return HttpResponse('zzz')