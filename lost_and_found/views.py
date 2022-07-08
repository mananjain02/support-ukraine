from PIL import Image
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .models import MissingPerson
from django.views.generic.edit import CreateView
from django.urls import reverse

# Create your views here.
class LostAndFoundView(View):
    def get(self, request):
        missing_person_list = MissingPerson.objects.all()
        context = {
            'missing_person_list': missing_person_list
        }
        return render(request, 'lost_and_found/lost_and_found.html', context)

    def post(self, request):
        pass


class ReportMissingView(CreateView):
    model = MissingPerson
    template_name = 'lost_and_found/report_missing.html'
    success_url = '/lost-and-found/'
    fields = "__all__"