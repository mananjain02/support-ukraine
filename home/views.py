from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.urls import reverse
from .models import SosMessage, SosUser, MedicalSos, MilitarySos
from django.contrib.auth import logout


class SosView(View):
    def get(self, request):
        if request.user.is_authenticated is False:
            return render(request, 'index.html')
        user_to_find = SosUser.objects.filter(user=request.user)
        if len(user_to_find) == 0:
            return render(request, 'home/profile.html', {
                'error_message': 'complete your profile to use SOS Ukraine'
            })

        context = {
            'role': user_to_find[0].role
        }
        if user_to_find[0].role == 'medical_unit':
            context['sos_messages'] = MedicalSos.objects.all()
        elif user_to_find[0].role == 'military_unit':
            context['sos_messages'] = MilitarySos.objects.all()
        return render(request, 'home/sos.html', context)

    def post(self, request):
        sos_message = SosMessage()
        sos_message.number_of_people = request.POST['number_of_people']
        sos_message.maps_location = request.POST['maps_location']
        sos_message.sosuser = SosUser.objects.get(user=request.user)
        if request.POST['medical_assistance'] == 'Yes':
            sos_message.medical_assistance = True
        else:
            sos_message.medical_assistance = False
        sos_message.save()

        if sos_message.medical_assistance == True:
            medical_sos_message = MedicalSos()
            medical_sos_message.sos_message = sos_message
            medical_sos_message.save()
            military_sos_message = MilitarySos()
            military_sos_message.sos_message = sos_message
            military_sos_message.save()
        else:
            military_sos_message = MilitarySos()
            military_sos_message.sos_message = sos_message
            military_sos_message.save()

        return HttpResponseRedirect(reverse('soshome'))


class ProfileView(View):
    def get(self, request):
        categories = ['individual', 'military_unit', 'medical_unit']
        user_details = SosUser.objects.filter(user=request.user)
        context = {}
        if len(user_details) == 0:
            user_details = SosUser()
            context = {
                'sosuser': user_details,
                'categories': categories,
            }
        else:
            context = {
                'sosuser': user_details[0],
                'categories': categories,
                'role': user_details[0].role
            }
        return render(request, 'home/profile.html', context)

    def post(self, request):
        user_to_find = SosUser.objects.filter(user=request.user)
        if len(user_to_find) != 0:
            user_to_edit = SosUser.objects.get(user=request.user)
            user_to_edit.role = request.POST['role']
            user_to_edit.save()
            return HttpResponseRedirect(reverse('soshome'))
        else:
            user_to_add = SosUser()
            user_to_add.name = request.user.username
            user_to_add.role = request.POST['role']
            user_to_add.email = request.user.email
            user_to_add.verified = True
            user_to_add.user = request.user
            user_to_add.save()
            return HttpResponseRedirect(reverse('soshome'))

def LogOut(request):
    logout(request)
    return HttpResponseRedirect(reverse('soshome'))

class PeopleRescuedView(View):
    def post(self, request):
        if request.POST['role'] == 'medical_unit':
            sos_rescued = MedicalSos.objects.get(id=request.POST['rescued_id'])
            sos_rescued.delete()
        else:
            sos_rescued = MilitarySos.objects.get(
                id=request.POST['rescued_id'])
            sos_rescued.delete()

        return HttpResponseRedirect(reverse('soshome'))
