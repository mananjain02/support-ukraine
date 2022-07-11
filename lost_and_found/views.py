from PIL import Image
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from requests import request
from .models import MissingPerson
from django.views.generic.edit import CreateView, FormView
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


class ReportMissingView(View):
    def get(self, request):
        return render(request, 'lost_and_found/report_missing.html')

    def post(self, request):
        missing_person = MissingPerson()
        missing_person.name = request.POST['name']
        missing_person.date_of_birth = request.POST['date_of_birth']
        missing_person.date_missing = request.POST['date_missing']
        missing_person.image = request.FILES['image']
        missing_person.birth_mark = request.POST['birth_mark']
        missing_person.place_seen_last_time = request.POST['place_seen_last_time']
        missing_person.save()
        return HttpResponseRedirect(reverse('lost_and_found'))

    